# Arquitetura do sistema

Esta pagina descreve a arquitetura prevista do **Ball Balancing Robot** como um sistema integrado de controle, visao computacional, embarcados e interface web.

## Visao geral

O sistema pode ser dividido em cinco blocos principais:

- **Captura de imagem:** camera posicionada para observar a plataforma.
- **Processamento visual:** software responsavel por detectar a bola e estimar sua posicao.
- **Controle:** calculo do erro e da resposta de controle para cada eixo.
- **Atuacao:** servomotores que inclinam fisicamente a mesa.
- **Interface web:** dashboard usado para monitorar, ajustar e controlar o sistema.

## Fluxo de dados

```text
Camera
  -> Processamento de imagem
  -> Posicao da bola
  -> Controlador
  -> Comandos para servomotores
  -> Movimento da plataforma
  -> Nova leitura pela camera
```

O ciclo forma uma malha fechada: a saida fisica da mesa altera a posicao da bola, e essa nova posicao volta para o software pela camera.

## Raspberry Pi

O Raspberry Pi atua como ponto central do sistema embarcado. Ele pode concentrar:

- captura da camera;
- processamento dos frames;
- execucao da logica de controle;
- comunicacao com servomotores ou controladores auxiliares;
- execucao do backend;
- exposicao da interface pela rede local.

## Visao computacional

A visao computacional transforma a imagem bruta da camera em uma medida util para controle.

Etapas comuns:

1. Captura do frame.
2. Pre-processamento para reduzir ruido.
3. Segmentacao da bola.
4. Identificacao do centro da bola.
5. Conversao para coordenadas relativas a mesa.
6. Envio da posicao para o controlador.

## Controle

O controlador recebe a posicao atual da bola e compara com a posicao desejada. O erro calculado indica para qual lado e com qual intensidade a plataforma deve inclinar.

Os parametros do controlador precisam ser ajustados experimentalmente. Ganhos muito baixos podem deixar a resposta lenta; ganhos muito altos podem gerar oscilacao.

## Dashboard e rede

A interface web transforma o projeto em uma aplicacao de IoT local. O usuario pode acessar o controle pelo navegador, inclusive em celular, desde que esteja conectado a mesma rede.

Funcoes possiveis:

- iniciar e pausar o controle;
- visualizar estado do sistema;
- alterar parametros;
- acompanhar posicao detectada;
- registrar observacoes de teste;
- reiniciar a calibracao.

## Pontos criticos

- Iluminacao consistente melhora a deteccao.
- Latencia de camera e processamento afeta diretamente a estabilidade.
- Folgas mecanicas prejudicam a repetibilidade.
- Posicionamento da camera altera a calibracao.
- Servomotores precisam de faixa, velocidade e alimentacao adequadas.
