# entrega-com-prazo

Aula 11 de Engenharia de Software · Ciência da Computação · Universidade Cruzeiro do Sul · 2026/2

Você vai percorrer um ciclo completo de mudança de software, do pedido à integração, com a IA participando de cada etapa e você decidindo em todas. O produto não é a função. O produto é o rastro que mostra como a função chegou ali.

## A regra de ouro

**O teste não se mexe para passar.** Se um teste está errado, o erro está no critério de aceitação, e critério se corrige na issue, à vista de todos.

## O caso

A coordenação quer um módulo que receba entregas de trabalho e aplique a regra de atraso. Foi isto que ela escreveu, com estas palavras:

1. Cada trabalho tem data e hora limite de entrega.
2. Entrega feita até o limite recebe a nota integral.
3. Entrega atrasada perde 10% da nota por dia iniciado de atraso.
4. O desconto por atraso não passa de 50%.
5. Depois de 5 dias de atraso o sistema não aceita mais a entrega.
6. Aluno com justificativa aprovada pela coordenação entrega sem desconto, dentro de um novo prazo definido por ela.
7. O professor pode reabrir a entrega para um aluno específico.
8. O sistema registra quem entregou, quando, e qual desconto foi aplicado.

Leia com atenção. O enunciado não é completo, e encontrar o que falta nele é parte do passo 2.

## Os seis passos

### 1. Preparar o ambiente

Entre na sua **conta pessoal** do GitHub, ative o Copilot Free nas configurações da conta, crie o seu repositório a partir deste modelo (botão **Use this template**) e abra no Codespaces (**Code** → aba **Codespaces** → **Create codespace on main**). Confirme que o ícone do Copilot aparece na barra lateral.

Conta gerenciada por uma organização não ativa o Copilot Free. Precisa ser pessoal.

**Entrega:** o link do seu repositório, postado no chat da turma.

### 2. A issue

Abra uma issue usando o modelo **Especificação** e escreva, nesta ordem:

- requisitos funcionais numerados, a partir das oito regras, um por comportamento;
- requisitos não funcionais com propriedade, métrica, valor e condição;
- a lista de ambiguidades em separado, ou seja, o que o enunciado não diz e você precisaria perguntar à coordenação;
- um critério de aceitação por requisito, no formato Dado / Quando / Então.

**Só depois de escrever tudo isso** peça ao Copilot Chat: *"Revise esta especificação e aponte ambiguidades que eu não listei."* Leia, julgue, e acrescente o que fizer sentido.

**Entrega:** a issue publicada.

### 3. Os testes

```bash
git checkout -b regra-de-atraso
```

Cole os seus critérios como comentário em `tests/test_nota.py`, peça ao Copilot um teste por critério com o arquivo aberto, e rode:

```bash
python -m pytest -v
```

**Todos falham.** É o resultado esperado: ainda não existe código. Um teste que falha antes de existir código prova que ele está mesmo testando alguma coisa.

**Entrega:** um teste por critério, todos falhando.

### 4. O código

Com o arquivo de teste aberto, peça o código de `calcular_nota_final`. Rode os testes. Quando falhar, **corrija o pedido, não o código na mão**: diga ao Copilot qual teste falhou e o que era esperado. Repita até ficar tudo verde.

**Entrega:** todos os testes passando.

### 5. Pull request e revisão

```bash
git add .
git commit -m "Aplica a regra de desconto por atraso"
git push -u origin regra-de-atraso
```

Abra o pull request no github.com referenciando a issue com `Closes #1` (o GitHub só reconhece palavras-chave em inglês). No texto, descreva o que fez e, principalmente, **qual decisão você tomou em cada ambiguidade**.

Volte ao Codespaces, selecione o conteúdo de `src/nota.py`, botão direito → **Copilot** → **Review and Comment**. Cole a revisão como comentário no seu pull request, dizendo que veio do Copilot.

**Entrega:** pull request aberto, ligado à issue, com a revisão colada como comentário.

### 6. Julgar e integrar

Responda cada item da revisão com **aceito**, **recuso** ou **adio**, e justifique cada recusa em uma linha. Recusa sem justificativa é teimosia; com justificativa é engenharia.

Aplique o que aceitou, rode os testes de novo, integre o pull request.

**Entrega:** pull request integrado, com cada item da revisão respondido.

## Como isso é corrigido

Pelo histórico do repositório, não por arquivo enviado. O que eu procuro não é se você aceitou muito ou pouco a revisão. É se cada decisão tem razão escrita. Um pull request com três recusas bem justificadas vale mais que um com tudo aceito em silêncio.

| Item | O que precisa estar lá |
| --- | --- |
| Repositório | público, criado a partir deste modelo |
| Issue | requisitos funcionais, requisitos não funcionais com métrica, ambiguidades e um critério por requisito |
| Ramo | nome que diz o que foi feito, com os commits da construção |
| Testes | um por critério de aceitação, todos passando no fim |
| Pull request | referenciando a issue, com as decisões tomadas nas ambiguidades |
| Revisão | colada no pull request, cada item aceito, recusado ou adiado, cada recusa justificada |
| Integração | pull request integrado ao ramo principal |

## Comandos que você vai usar

```bash
python -m pytest -v          # roda todos os testes, mostrando um por linha
python -m pytest -k atraso   # roda só os testes com "atraso" no nome
git status                   # o que mudou e ainda não foi registrado
git log --oneline            # o histórico do que você já fez
```
