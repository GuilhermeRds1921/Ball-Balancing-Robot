# Operacao e testes

Este documento organiza os cuidados de operacao e testes do **Ball Balancing Robot**. O repositorio ainda nao contem a implementacao completa, entao os passos abaixo servem como roteiro tecnico para montagem, calibracao e validacao.

## Preparacao

Antes de iniciar os testes:

- fixe a mesa em uma bancada estavel;
- confira a alimentacao dos servomotores;
- verifique cabos, conectores e aterramento;
- posicione a camera para enxergar toda a area util da plataforma;
- garanta iluminacao constante;
- confirme que o Raspberry Pi ou computador esta na rede;
- acesse o dashboard pelo navegador.

## Calibracao visual

A calibracao da visao computacional deve confirmar:

- se a bola e detectada corretamente;
- se falsos positivos foram reduzidos;
- se o centro da bola esta coerente com a imagem;
- se as coordenadas aumentam no sentido esperado;
- se o centro da mesa corresponde ao alvo do controle.

Mudancas de luz, cor da bola, reflexo ou angulo de camera podem exigir nova calibracao.

## Calibracao dos atuadores

Antes de ativar controle automatico, e importante testar os servomotores separadamente:

- posicao neutra;
- limite minimo e maximo;
- sentido de movimento;
- resposta de cada eixo;
- vibracao ou travamento;
- aquecimento;
- estabilidade da fonte.

## Teste manual

O modo manual e util para validar a mecanica antes da malha fechada:

1. Envie pequenos comandos de inclinacao.
2. Observe se a mesa responde no eixo correto.
3. Verifique se a inclinacao esta proporcional ao comando.
4. Confirme se nenhum servo atinge limite fisico.
5. Ajuste offsets e limites, se necessario.

## Teste automatico

Com a visao e os atuadores validados:

1. Posicione a bola proxima ao centro.
2. Inicie a leitura da camera.
3. Ative o controle com ganhos conservadores.
4. Observe a resposta da bola.
5. Ajuste os ganhos gradualmente.
6. Registre os parametros que apresentarem melhor estabilidade.

## Acesso pelo celular

Quando o backend estiver executando na rede local, o dashboard pode ser acessado por outro dispositivo usando o endereco IP do Raspberry Pi ou computador.

Exemplo de formato:

```text
http://<ip-do-dispositivo>:<porta>
```

Esse acesso permite controlar e monitorar a mesa sem conectar monitor, teclado ou mouse diretamente ao sistema embarcado.

## Registro de resultados

Para documentar os testes, recomenda-se registrar:

- data do teste;
- condicoes de iluminacao;
- posicao da camera;
- bola utilizada;
- ganhos do controlador;
- tempo de resposta;
- ocorrencia de oscilacao;
- falhas de deteccao;
- observacoes mecanicas.

## Pendencias de documentacao

Quando o codigo completo for incorporado ao repositorio, esta pagina deve receber:

- comandos reais de instalacao;
- dependencias do backend;
- instrucoes da interface web;
- diagrama de ligacao dos servomotores;
- exemplo de configuracao;
- imagens ou links publicos para demonstracoes;
- procedimento final de execucao.
