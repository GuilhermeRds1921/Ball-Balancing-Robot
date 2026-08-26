# Ball Balancing Robot

![Controle](https://img.shields.io/badge/Controle-Robotnik-149ddd?style=for-the-badge) ![Visão computacional](https://img.shields.io/badge/Visão%20computacional-Robotnik-149ddd?style=for-the-badge) ![Robótica](https://img.shields.io/badge/Robótica-Robotnik-149ddd?style=for-the-badge) ![OpenCV](https://img.shields.io/badge/OpenCV-Robotnik-149ddd?style=for-the-badge) ![Servomotores](https://img.shields.io/badge/Servomotores-Robotnik-149ddd?style=for-the-badge)

> Mesa robótica para equilibrar uma bola usando visão computacional, controle e atuadores.

<p align="center">
  <img src="mesa-equilibrio.png" alt="Imagem de capa do projeto Ball Balancing Robot" width="400" />
</p>

## Sumário

- [Visão geral](#visão-geral)
- [Objetivos](#objetivos)
- [Principais recursos](#principais-recursos)
- [Arquitetura do projeto](#arquitetura-do-projeto)
- [Hardware](#hardware)
- [Software](#software)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Como usar](#como-usar)
- [Aplicação em divulgação científica](#aplicação-em-divulgação-científica)
- [Continuidade do projeto](#continuidade-do-projeto)
- [Referências](#referências)

## Visão geral

A mesa de equilíbrio de bola é um protótipo de robótica e controle que busca manter uma bola em posição desejada por meio da leitura da posição e da atuação em uma plataforma inclinável. O projeto é útil para demonstrações de controle, sensores, processamento de imagem, atuadores e integração software-hardware.

Este repositório faz parte da organização **Robotnik - DAINF-PB**, projeto de extensão do DAINF da UTFPR - Campus Pato Branco voltado à robótica, prototipagem e divulgação científica.

## Objetivos

- Documentar a arquitetura geral da mesa de equilíbrio.
- Registrar hardware, software, controle e lógica de atuação.
- Facilitar futuras manutenções e melhorias do protótipo.
- Servir como referência didática para conceitos de controle e robótica.

## Principais recursos

- Leitura da posição da bola.
- Atuação em plataforma por servomotores ou mecanismo equivalente.
- Aplicação de conceitos de controle em malha fechada.
- Potencial integração com visão computacional e interface de monitoramento.

## Arquitetura do projeto

A arquitetura pode ser entendida em quatro camadas principais:

| Camada | Função |
|---|---|
| Mecânica | Estrutura física, peças impressas em 3D, suportes e montagem. |
| Eletrônica | Microcontroladores, sensores, atuadores, alimentação e conexões. |
| Software embarcado | Código de controle, leitura de entradas, processamento e acionamento. |
| Demonstração | Uso do protótipo em oficinas, feiras, escolas e eventos de divulgação. |

## Hardware

- Plataforma mecânica inclinável
- Servomotores ou atuadores equivalentes
- Câmera ou sensor para detecção da bola
- Microcontrolador ou computador embarcado
- Fonte de alimentação e estrutura de suporte

## Software

- Linguagem e ambiente conforme implementação do repositório
- OpenCV ou biblioteca equivalente, se utilizada
- Algoritmo de controle
- Rotina de leitura, processamento e atuação

## Estrutura do repositório

- `README.md - documentação principal`
- Arquivos de código e configuração conforme implementação do projeto

## Como usar

> Esta seção deve ser ajustada conforme a versão atual do código e dos arquivos do repositório.

1. Clone o repositório:

```bash
git clone https://github.com/DAINF-PB-Robotnik/Ball-Balancing-Robot.git
cd Ball-Balancing-Robot
```

2. Confira as pastas de código, peças, esquemáticos e documentação.
3. Instale as dependências necessárias para o ambiente usado no projeto.
4. Faça a montagem elétrica e mecânica seguindo as conexões documentadas.
5. Carregue o código no microcontrolador ou execute o software principal.
6. Teste por etapas antes de usar o protótipo completo.

## Aplicação em divulgação científica

O projeto pode ser usado em atividades de extensão para apresentar conceitos de robótica e engenharia de forma visual e prática. Em eventos, oficinas e visitas técnicas, o protótipo ajuda a conectar assuntos como programação, eletrônica, sensores, impressão 3D, controle e resolução de problemas com uma demonstração concreta.

## Continuidade do projeto

Sugestões para evolução:

- Atualizar a documentação com fotos reais da montagem.
- Adicionar diagramas de ligação elétrica.
- Registrar vídeos curtos de funcionamento.
- Criar uma seção de problemas comuns e soluções.
- Padronizar nomes de arquivos e dependências.
- Adicionar instruções de segurança para alimentação, motores e partes móveis.
- Criar uma versão em artigo técnico a partir do arquivo LaTeX deste pacote.

## Referências

- Conceitos de controle em malha fechada
- Conceitos de visão computacional aplicada à robótica
- Projetos didáticos de ball balancing robot

## Organização

**Robotnik - DAINF-PB**  
Departamento Acadêmico de Informática - UTFPR, Campus Pato Branco.

