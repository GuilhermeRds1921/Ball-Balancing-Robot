from pathlib import Path
import re

CANDIDATES = [
    Path("App.js"),
    Path("src/App.js"),
    Path("src/App.jsx"),
]


def backup(path: Path) -> None:
    backup_path = path.with_suffix(path.suffix + ".backup_sem_stop_emergencia")

    if not backup_path.exists():
        backup_path.write_text(
            path.read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        print(f"Backup criado: {backup_path}")
    else:
        print(f"Backup já existe: {backup_path}")


def remove_button_by_text(text: str, button_text: str) -> str:
    pattern = re.compile(
        r"\n\s*<button\b(?:(?!</button>).)*?"
        + re.escape(button_text)
        + r"(?:(?!</button>).)*?</button>\s*",
        flags=re.DOTALL,
    )

    return pattern.sub("\n", text)


def patch_start_balancar(text: str) -> str:
    pattern = re.compile(
        r"const\s+startBalancar\s*=\s*async\s*\(\)\s*=>\s*\{.*?\};",
        flags=re.DOTALL,
    )

    replacement = """const startBalancar = async () => {
    await postJson("/routine/bambole");
  };"""

    if "const startBalancar" in text:
        text = pattern.sub(replacement, text)

    return text


def patch_polling(text: str) -> str:
    text = text.replace("setInterval(fetchData, 400)", "setInterval(fetchData, 200)")
    text = text.replace("setInterval(fetchData, 300)", "setInterval(fetchData, 200)")
    text = text.replace("setInterval(fetchData, 250)", "setInterval(fetchData, 200)")

    text = text.replace(
        "transition: left 120ms linear, top 120ms linear, opacity 120ms ease;",
        "transition: left 80ms linear, top 80ms linear, opacity 80ms ease;",
    )

    return text


def clean_unused_css(text: str) -> str:
    css_blocks = [
        r"\n\s*\.redwood-button\s*\{.*?\}\s*",
        r"\n\s*\.emergency-button\s*\{.*?\}\s*",
        r"\n\s*\.emergency-button\s+\.button-icon\s*\{.*?\}\s*",
    ]

    for block in css_blocks:
        text = re.sub(block, "\n", text, flags=re.DOTALL)

    return text


def patch_app(path: Path) -> None:
    backup(path)

    text = path.read_text(encoding="utf-8")

    original = text

    text = remove_button_by_text(text, "Stop PWM")
    text = remove_button_by_text(text, "Emergência")
    text = remove_button_by_text(text, "EMERGÊNCIA")
    text = patch_start_balancar(text)
    text = patch_polling(text)
    text = clean_unused_css(text)

    if text == original:
        print("Nenhuma alteração detectada. Talvez o App.js já esteja ajustado.")
    else:
        path.write_text(text, encoding="utf-8")
        print(f"App atualizado: {path}")

    print()
    print("Alterações aplicadas:")
    print("- removeu botão Stop PWM")
    print("- removeu botão Emergência")
    print("- Balançar chama /routine/bambole")
    print("- polling da telemetria ajustado para 200 ms")
    print("- animação da bolinha ajustada para 80 ms")


def main() -> None:
    for path in CANDIDATES:
        if path.exists():
            patch_app(path)
            return

    raise FileNotFoundError(
        "Não encontrei App.js, src/App.js ou src/App.jsx. Rode este script na pasta do frontend."
    )


if __name__ == "__main__":
    main()
