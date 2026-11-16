---
name: Especificação
about: Requisitos, ambiguidades e critérios de aceitação da mudança
title: 'Aplicar a regra de desconto por atraso na entrega de trabalhos'
labels: especificacao
---

## Requisitos funcionais

Um por comportamento, numerados. Escreva o que o sistema faz, não como ele faz.

| ID | Requisito |
| --- | --- |
| RF-001 | |
| RF-002 | |
| RF-003 | |

## Requisitos não funcionais

Com propriedade, métrica, valor e condição. Se não dá para medir, ainda não é requisito.

| ID | Propriedade | Métrica | Valor | Condição |
| --- | --- | --- | --- | --- |
| RNF-001 | | | | |

## Ambiguidades do enunciado

O que a coordenação não disse e eu precisaria perguntar antes de programar. Esta lista não entra na tabela de requisitos: ela é a pergunta, não a resposta.

1.
2.

## Decisões tomadas

Para cada ambiguidade acima, o que eu decidi e por quê. É esta seção que vai ser cobrada no pull request.

| Ambiguidade | Decisão | Por quê |
| --- | --- | --- |
| | | |

## Critérios de aceitação

Um por requisito funcional, no formato Dado / Quando / Então. Cada um destes vira um teste no passo 3.

### RF-001

```
Dado
Quando
Então
```

### RF-002

```
Dado
Quando
Então
```

## Assinatura da função

O que entra, de que tipo, e o que sai. Decida aqui, antes de escrever qualquer teste.

```python
calcular_nota_final(nota, prazo, entrega, justificativa_aprovada, novo_prazo)
# retorna:
```
