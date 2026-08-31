# Rede Wi‑Fi do Raspberry Pi

A ideia do projeto e que o Raspberry Pi 4 funcione como ponto de acesso Wi‑Fi local, criando uma rede propria para o sistema. Assim, o celular e o notebook podem se conectar diretamente ao Raspberry e abrir a interface web sem depender de internet externa.

## Topologia da rede

```text
Celular / Notebook
        |
        | Wi‑Fi (SSID: BallBalancingRobot)
        v
Raspberry Pi 4 (Access Point)
  |
  +-- Frontend: http://192.168.50.1:3000
  |
  +-- Backend:  http://192.168.50.1:8000
  |
  +-- Camera / servomotores / controle
```

## Enderecos esperados

- Rede Wi‑Fi do Raspberry: `BallBalancingRobot`
- IP do Raspberry em AP mode: `192.168.50.1`
- Backend: `http://192.168.50.1:8000`
- Frontend: `http://192.168.50.1:3000`
- Opcionalmente, via NGINX/serva: `http://192.168.50.1`

## Configuracao do Raspberry Pi como AP

No Raspberry Pi, instale os pacotes:

```bash
sudo apt update
sudo apt install -y hostapd dnsmasq
```

Configure a interface Wi‑Fi do Raspberry para ter IP fixo:

```bash
sudo nano /etc/dhcpcd.conf
```

Adicione:

```text
interface wlan0
static ip_address=192.168.50.1/24
nohook wpa_supplicant
```

Ative a rede no boot:

```bash
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
```

Configure o Host AP:

```bash
sudo nano /etc/hostapd/hostapd.conf
```

Exemplo:

```text
country_code=BR
interface=wlan0
ssid=BallBalancingRobot
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=ballbot123
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

Ative:

```bash
sudo nano /etc/default/hostapd
```

Adicione:

```text
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

Configure o DHCP do AP:

```bash
sudo nano /etc/dnsmasq.conf
```

Adicione:

```text
interface=wlan0
dhcp-range=192.168.50.10,192.168.50.50,255.255.255.0,12h
```

Reinicie os servicos:

```bash
sudo systemctl restart hostapd
sudo systemctl restart dnsmasq
sudo systemctl restart dhcpcd
```

## Backend na rede local do Pi

O backend deve expor a interface em `0.0.0.0` para aceitar conexoes da rede local:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

A API fica acessivel em:

```text
http://192.168.50.1:8000
```

## Frontend na mesma rede

O frontend deve apontar para a API do propio Raspberry:

```env
REACT_APP_API_URL=http://192.168.50.1:8000
```

Rodando em desenvolvimento:

```bash
cd frontend
npm install
cp .env.example .env
npm start -- --host 0.0.0.0 --port 3000
```

A interface fica acessivel em:

```text
http://192.168.50.1:3000
```

## Conexao do celular ou notebook

1. Conecte-se ao Wi‑Fi `BallBalancingRobot`.
2. Use a senha configurada no `hostapd.conf`.
3. Abra o navegador e acesse:
   - `http://192.168.50.1:3000` para o frontend em desenvolvimento;
   - ou `http://192.168.50.1` se estiver sendo servido por um proxy ou build de producao.
4. O frontend ja deve consumir o backend em `http://192.168.50.1:8000`.

## Observacoes importantes

- A porta 8000 precisa estar liberada para o backend.
- O frontend deve evitar hardcoded IPs locais do notebook/PC e usar `REACT_APP_API_URL`.
- Em producao, vale usar um servidor web como NGINX para servir o build do frontend na porta 80, apontando para o backend em 8000.
- Para um ambiente mais robusto, e recomendado usar um sistema de init para iniciar backend e frontend automaticamente ao ligar o Raspberry.
