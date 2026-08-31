# Ball Balancing Robot

Projeto de bancada robotica para equilibrar uma bola em uma mesa inclinavel usando visao computacional, controle e dashboard web.

Este repositorio foi organizado em duas partes principais:

- backend/: API em Python com FastAPI, processamento de imagem e controle do sistema.
- frontend/: interface web em React para monitoramento e acionamento.
- docs/: documentacao de arquitetura e operacao.

Portfolio: [guilhermerds1921.github.io](https://guilhermerds1921.github.io/)
Pagina do projeto: [Mesa Robotica de Equilibrio de Bola](https://guilhermerds1921.github.io/projects/ball-balancing-robot/)

## Objetivo

O objetivo e manter a bola no centro da mesa por meio de uma malha de controle fechada, usando:

- camera para detectar a bola;
- processamento de imagem para obter a posicao;
- algoritmo de controle para calcular a inclinacao ideal;
- servomotores para ajustar a plataforma;
- interface web para monitorar e ajustar parametros.

## Estrutura do repositorio

```text
Ball-Balancing-Robot/
├── backend/
│   ├── camera.py
│   ├── camera_pc.py
│   ├── main.py
│   ├── requirements.txt
│   ├── simulator.py
│   └── vision.py
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   └── .env.example
├── docs/
│   ├── architecture.md
│   └── operation.md
├── .gitignore
├── README.md
└── .git/
```

## Backend

O backend e responsavel por expor a API do sistema, receber frames da camera e atualizar a posicao da bola. Ele tambem recebe os ajustes de PID e disponibiliza a stream video e dados de telemetry para a interface web.

### Requisitos

- Python 3.10+
- pip
- OpenCV
- FastAPI

### Execucao

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Frontend

O frontend e uma interface web em React para:

- visualizar status do sistema;
- acompanhar a posicao da bola;
- ajustar parametros de controle;
- enviar comandos para a rotina de equilibrio.

### Execucao

```bash
cd frontend
npm install
cp .env.example .env
npm start
```

O arquivo `.env` deve apontar para a URL do backend, por exemplo:

```env
REACT_APP_API_URL=http://localhost:8000
```

Quando o backend estiver rodando em outra maquina, troque esse valor para o IP ou hostname correto.

## Documentacao

- [Arquitetura do sistema](docs/architecture.md)
- [Operacao e testes](docs/operation.md)

## Tecnologias

- Python
- FastAPI
- OpenCV
- React
- JavaScript
- Raspberry Pi
- Visao computacional
- Controle de mesa inclinavel

## Observacoes

Este projeto ainda e uma base de desenvolvimento e experimentacao, com a parte de visao e controle em evolucao. A estrutura foi organizada para facilitar a separacao entre o codigo do hardware/servidor e a interface do usuario.

## Referencias

- [Pagina do projeto no portfolio](https://guilhermerds1921.github.io/projects/ball-balancing-robot/)
- [Galeria do projeto](https://guilhermerds1921.github.io/gallery/ball-balancing-robot/)
- [Robotnik no portfolio](https://guilhermerds1921.github.io/projects/robotnik/)
- [Instructables: Ball Balancing Robot](https://www.instructables.com/Ball-Balancing-Robot/)
