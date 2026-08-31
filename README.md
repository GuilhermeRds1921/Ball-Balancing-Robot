# Ball Balancing Robot

Documentacao tecnica do projeto **Ball Balancing Robot**, tambem apresentado no portfolio como **Mesa Robotica de Equilibrio de Bola**.

O projeto consiste em uma plataforma robotica capaz de detectar a posicao de uma bola por visao computacional e atuar sobre a inclinacao da mesa para tentar manter a bola equilibrada. Ele foi desenvolvido no contexto da Robotnik / UTFPR-PB como uma aplicacao pratica de sistemas de controle, sistemas embarcados, IoT, dashboard web e integracao hardware-software.

Portfolio: [guilhermerds1921.github.io](https://guilhermerds1921.github.io/)<br>
Pagina do projeto: [Mesa Robotica de Equilibrio de Bola](https://guilhermerds1921.github.io/projects/ball-balancing-robot/)

## Objetivo

O objetivo do projeto e construir uma mesa robotica que consiga:

- identificar a bola sobre a plataforma;
- calcular a posicao da bola em relacao ao centro;
- estimar o erro de controle nos eixos da mesa;
- converter esse erro em comandos para os servomotores;
- permitir monitoramento e ajustes por uma interface web;
- demonstrar, de forma pratica, conceitos de controle, visao computacional e IoT.

## Problema

Equilibrar uma bola sobre uma superficie movel e um problema classico de controle: pequenas variacoes de inclinacao alteram a velocidade e a direcao da bola, exigindo leitura continua do estado do sistema e resposta rapida dos atuadores.

Neste projeto, a mesa funciona como uma bancada experimental. A camera fornece a realimentacao visual, o software estima a posicao da bola e o controlador calcula como a plataforma deve inclinar para reduzir o erro entre a posicao atual e a posicao desejada.

## Como o sistema funciona

Fluxo geral:

1. A camera captura a imagem da plataforma.
2. O software processa a imagem e detecta a bola.
3. A posicao da bola e convertida para coordenadas de controle.
4. O controlador calcula o erro em relacao ao alvo.
5. O backend envia comandos para os servomotores.
6. A mesa altera sua inclinacao.
7. O dashboard web exibe o estado do sistema e permite interacao do usuario.

Esse ciclo se repete continuamente, formando uma malha de controle fechada.

## Deteccao da bola

A deteccao da bola e baseada em visao computacional. Em uma implementacao tipica do projeto, a camera conectada ao Raspberry Pi captura frames da mesa e o software processa essas imagens para localizar a bola.

O processamento pode envolver:

- conversao de espaco de cor;
- segmentacao por cor ou contraste;
- filtragem de ruido;
- deteccao de contornos ou regioes circulares;
- calculo do centro da bola no frame;
- conversao da posicao da imagem para o sistema de coordenadas da mesa.

O resultado dessa etapa e a posicao aproximada da bola, usada como entrada do controlador.

## Controle da mesa

O controle atua sobre a inclinacao da plataforma. A posicao desejada normalmente e o centro da mesa, e o erro e calculado pela diferenca entre a posicao atual da bola e esse ponto de referencia.

Com base nesse erro, o controlador calcula a correcao necessaria para cada eixo. Essa correcao e traduzida em angulos ou comandos de posicao para os servomotores, que inclinam fisicamente a plataforma.

Na pratica, o comportamento do sistema depende de fatores como:

- taxa de captura da camera;
- latencia de processamento;
- velocidade dos servomotores;
- calibracao mecanica da mesa;
- ganhos do controlador;
- iluminacao do ambiente;
- atrito e peso da bola.

## Dashboard web e IoT

O projeto tambem explora conceitos de IoT ao permitir que o sistema fisico seja monitorado e controlado por rede.

A interface web pode ser acessada por navegador, inclusive em celular, desde que o dispositivo esteja na mesma rede do Raspberry Pi ou do computador que executa o backend. Isso permite acompanhar o estado do sistema sem depender de uma tela conectada diretamente ao hardware.

O dashboard pode reunir recursos como:

- visualizacao do status do sistema;
- leitura da posicao detectada da bola;
- comandos de inicio, pausa e reset;
- ajustes de parametros de controle;
- exibicao de dados de teste;
- acompanhamento da resposta da mesa.

## Tecnologias

- Raspberry Pi
- Camera
- Servomotores
- C/C++
- Python
- OpenCV
- FastAPI
- HTML, CSS e JavaScript
- Comunicacao via rede local
- Sistemas embarcados
- Visao computacional
- Sistemas de controle
- IoT

## Participacao de Guilherme Rodrigues

Minha participacao no projeto envolveu a construcao da solucao como um sistema integrado, conectando hardware, software embarcado, controle e interface web.

Principais frentes de participacao:

- estudo da arquitetura geral da mesa robotica;
- integracao entre camera, processamento e atuadores;
- desenvolvimento e testes da logica de controle;
- organizacao do backend para comunicar a interface com o sistema fisico;
- criacao de interface web/dashboard para controle e acompanhamento;
- testes em bancada, ajustes e validacao do comportamento da mesa;
- documentacao tecnica do projeto para uso no portfolio e no GitHub.

## Como rodar

O repositorio ainda esta em organizacao e nao contem, neste momento, todos os arquivos necessarios para executar o sistema completo diretamente.

Quando o codigo completo estiver publicado, a execucao devera documentar:

- dependencias do backend;
- versao do Python ou compilador usado;
- configuracao da camera;
- configuracao dos servomotores;
- comandos para iniciar o backend;
- comandos para iniciar a interface web;
- endereco de acesso pelo navegador ou celular;
- passos de calibracao da mesa.

Enquanto isso, este repositorio funciona como documentacao tecnica do projeto e ponto de referencia para a pagina do portfolio.

## Documentacao

- [Arquitetura do sistema](docs/architecture.md)
- [Operacao e testes](docs/operation.md)

## Referencias

- [Pagina do projeto no portfolio](https://guilhermerds1921.github.io/projects/ball-balancing-robot/)
- [Galeria do projeto](https://guilhermerds1921.github.io/gallery/ball-balancing-robot/)
- [Robotnik no portfolio](https://guilhermerds1921.github.io/projects/robotnik/)
- [Instructables: Ball Balancing Robot](https://www.instructables.com/Ball-Balancing-Robot/)
