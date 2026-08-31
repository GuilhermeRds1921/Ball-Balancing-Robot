# Frontend - Ball Balancing Robot

Este diretório contém a interface web do projeto: um dashboard em React para monitorar a posição da bola, ajustar ganhos e controlar a rotina da mesa.

## Tecnologias

- React
- Create React App
- JavaScript
- Fetch para comunicação com o backend

## Configuração

1. Instale as dependências:

   ```bash
   npm install
   ```

2. Crie um arquivo de ambiente com a URL do backend:

   ```bash
   cp .env.example .env
   ```

   Exemplo:

   ```env
   REACT_APP_API_URL=http://localhost:8000
   ```

   Em um Raspberry Pi ou outra máquina remota, substitua pelo endereço do backend correspondente.

## Execução

```bash
npm start
```

A aplicação será aberta em http://localhost:3000.

## Build de produção

```bash
npm run build
```

O build gerado fica na pasta `build/`.
