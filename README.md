Atividade prática: um ciclo completo de software, com IA dentro
Aula 11 de Engenharia de Software · Ciência da Computação · Universidade Cruzeiro do Sul · 2026/2

Repositório da turma: https://github.com/Msbastos04/16.11.26_SA_ENG

Leia isto primeiro
Você vai percorrer um ciclo completo de mudança de software, do pedido à entrega, com a IA participando de quatro momentos e você decidindo em todos.

O produto não é a função que você vai escrever. O produto é o rastro que mostra como ela chegou ali: a especificação, as lacunas que você encontrou, as decisões que tomou, os testes que provam o comportamento, e o julgamento que você fez da revisão automática.

Existe um único comando nesta oficina, e é o que roda os testes. Todo o resto é clicar num botão que está na tela. Se você achar que precisa digitar um comando, provavelmente existe um botão e você não achou. Chame o professor.

O que você entrega como evidência
Você entrega um link: o do seu repositório. Não há arquivo para enviar, nem relatório, nem formulário. A correção é feita abrindo o repositório e lendo o histórico.

Dentro dele, estas sete evidências precisam existir e estar visíveis:

#	Evidência	Onde eu abro para conferir	Sai do passo
1	Repositório público, chamado entrega-com-prazo	Em github.com/SEU-USUARIO/entrega-com-prazo, com o histórico de commits do repositório da turma	1
2	Issue publicada, com requisitos, ambiguidades, decisões e critérios	Aba Issues	2
3	Ramo com os commits da sua construção	Aba Code, no seletor de ramos	3 a 5
4	Um teste por critério de aceitação	Arquivo tests/test_nota.py	3
5	Código com todos os testes passando, e a prova disso	Arquivo src/nota.py, e a saída do pytest colada no pull request	4
6	Pull request ligado à issue, com a revisão colada como comentário	Aba Pull requests	5
7	Pull request integrado, com cada item da revisão respondido	O pull request aparece marcado como Merged, em roxo	6
A evidência que some se você não guardar
Os testes rodam no terminal e a saída desaparece quando você fecha o Codespace. Depois que tudo ficar verde, copie as últimas linhas do terminal e cole no texto do seu pull request, assim:

tests/test_nota.py::test_entrega_no_prazo PASSED      [ 14%]
...
============== 7 passed in 0.04s ==============
Sem isso, não existe registro de que os testes passaram.

Como postar no Blackboard
Uma linha, neste formato:

Nome completo:
Link do repositório: https://github.com/SEU-USUARIO/SEU-REPOSITORIO
Quatro palavras que você precisa saber
O repositório é uma pasta com memória: toda vez que você diz "pronto, guarda isso", ele tira uma foto do estado de todos os arquivos e guarda para sempre, com o seu nome, a data e o motivo que você escreveu. Essa foto chama commit.

Palavra	O que é	Onde fica
Issue	A ordem de serviço. Alguém pediu algo e escreveu o que quer	Aba Issues, no topo do repositório
Ramo	A bancada de trabalho. Você não mexe na peça em produção, puxa uma cópia	Canto inferior esquerdo do editor, onde está escrito main
Pull request	A entrega para inspeção. "Olhem o que eu fiz e me digam se pode entrar"	Aba Pull requests, no topo do repositório
Merge	O aceite. A inspeção passou e o trabalho entra na linha principal	Botão verde dentro do pull request
A regra de ouro
O teste não se mexe para passar. Se um teste está errado, o erro está no critério de aceitação, e critério se corrige na issue, à vista de todos. Esse é o único movimento proibido da atividade, e o histórico do repositório mostra quando acontece.

O caso
A coordenação quer um módulo que receba entregas de trabalho e aplique a regra de atraso. Foi isto que ela escreveu, com estas palavras:

Cada trabalho tem data e hora limite de entrega.
Entrega feita até o limite recebe a nota integral.
Entrega atrasada perde 10% da nota por dia iniciado de atraso.
O desconto por atraso não passa de 50%.
Depois de 5 dias de atraso o sistema não aceita mais a entrega.
Aluno com justificativa aprovada pela coordenação entrega sem desconto, dentro de um novo prazo definido por ela.
O professor pode reabrir a entrega para um aluno específico.
O sistema registra quem entregou, quando, e qual desconto foi aplicado.
Leia com atenção. O enunciado não está completo, e encontrar o que falta nele é parte do passo 2.

Os seis passos
Passo 1. Preparar o ambiente (20 min)
No canto superior direito do GitHub, clique no sinal de + e escolha Import repository.
No campo da URL do repositório de origem, cole: https://github.com/Msbastos04/16.11.26_SA_ENG
Em Repository name, escreva exatamente entrega-com-prazo, em minúsculas e com os hifens. Deixe marcado Public e clique em Begin import. Leva um ou dois minutos.
Quando terminar, abra o seu repositório: botão Code, aba Codespaces, botão Create codespace on main. Leva cerca de um minuto e abre um editor dentro do navegador.
Se aparecer Entrar no canto inferior direito do editor, clique e autorize. É o Copilot pedindo permissão. Sem isso ele não sugere nada.
Teste: abra src/nota.py, escreva um comentário numa linha nova e espere dois segundos. Deve aparecer um texto cinza claro sugerindo código sozinho. Apague o que você digitou depois do teste.
Evidência produzida: o repositório existe e é seu.

Passo 2. A issue (25 min)
Aqui você escreve a especificação. A IA só entra no fim, e como crítica.

Aba Issues, botão verde New issue. Escolha o modelo Especificação e clique em Get started. O formulário já vem dividido nas seções certas.
Preencha os requisitos funcionais, numerados, a partir das oito regras. Um requisito por comportamento.
Preencha os requisitos não funcionais, com propriedade, métrica, valor e condição. Se não dá para medir, ainda não é requisito.
Liste as ambiguidades: o que o enunciado não diz e você precisaria perguntar à coordenação antes de programar.
Preencha a tabela de decisões: o que você decidiu em cada ambiguidade e por quê.
Escreva um critério de aceitação por requisito, no formato Dado / Quando / Então. Cada um vira um teste no passo 3.
Só agora abra o Copilot Chat e peça: "Revise esta especificação e aponte ambiguidades que eu não listei." Leia, julgue, acrescente o que fizer sentido.
Publique a issue.
Onde a IA entra: como crítica da sua especificação, depois que você escreveu. Ela aponta lacunas, mas quem decide o que cada lacuna significa é você.

Evidência produzida: a issue publicada.

Passo 3. Os testes (30 min)
Crie o seu ramo: no editor, canto inferior esquerdo, onde está escrito main. Clique, escolha Create new branch, dê um nome que diga o que você vai fazer.
Abra tests/test_nota.py.
Cole os seus critérios como comentário no topo do arquivo. Os seus, do passo anterior, inteiros.
Peça ao Copilot um teste por critério, com o arquivo aberto. Confira se cada teste verifica o que o critério dizia, e não outra coisa.
No terminal, rode:
python -m pytest -v
Todos falham, e é o resultado esperado: ainda não existe código. Um teste que falha antes de existir código prova que ele está mesmo testando alguma coisa.

Onde a IA entra: como tradutora. Ela escreve o teste, mas quem definiu o que precisa ser provado foi você, no passo 2.

Evidência produzida: o ramo e o arquivo de testes.

Passo 4. O código (25 min)
Com o arquivo de teste aberto, peça ao Copilot o código de calcular_nota_final. Ele enxerga o que está aberto no editor, e o teste é a melhor especificação que existe.
Rode python -m pytest -v e olhe quantos passaram.
Quando falhar, conserte o pedido, não o código na mão. Diga ao Copilot qual teste falhou, qual valor veio e qual era esperado.
Repita até ficar tudo verde.
Copie as últimas linhas do terminal. Você vai colar no pull request, no passo 5.
Exemplo do que você vai ver quando a IA errar:

>       assert resultado.nota_final == 9.0
E       assert 10.0 == 9.0
O código estava bem escrito e parecia correto. O teste pegou em dois centésimos de segundo, e disse exatamente o número que veio e o número que era esperado.

Onde a IA entra: como executora. Ela digita a maior parte do código, mas quem diz que está pronto é o teste, não a aparência do que ela escreveu.

Evidência produzida: o código, e a saída verde do pytest.

Passo 5. Pull request e revisão (25 min)
Guarde o seu trabalho: barra lateral esquerda do editor, ícone de ramificação. Escreva uma mensagem dizendo o que mudou e clique no visto.
Envie: botão azul Publish Branch, logo abaixo da caixa de mensagem.
Volte ao GitHub. Aparece uma tarja amarela com o botão Compare & pull request. Clique.
No texto do pull request, escreva:
Closes #1, para ligar à sua issue. O GitHub só reconhece palavras-chave em inglês, então Fecha #1 não funciona.
o que você fez e qual decisão tomou em cada ambiguidade;
a saída verde do pytest que você copiou no passo 4.
Peça a revisão: no editor, selecione o conteúdo de src/nota.py, botão direito, Copilot, Review and Comment. Cole o resultado como comentário no pull request, dizendo que veio do Copilot.
Onde a IA entra: como revisora, não como juíza. Ela produz observações; o veredito é seu.

Evidência produzida: o pull request com tudo dentro.

Passo 6. Julgar e integrar (15 min)
Responda cada item da revisão com aceito, recuso ou adio. Os três são respostas legítimas e ninguém precisa aceitar tudo.
Justifique cada recusa em uma linha. Recusa sem justificativa é teimosia; com justificativa é engenharia.
Aplique o que aceitou e rode os testes de novo. Correção que quebra teste não é correção.
Clique em Merge pull request.
Aqui a IA não entra, e é de propósito. O pull request integrado tem um nome em cima, e esse nome responde pelo que o sistema faz.

Evidência produzida: o merge, e a discussão registrada.

Como isto é corrigido
Pelo histórico do repositório. O que eu procuro não é se você aceitou muito ou pouco a revisão. É se cada decisão tem razão escrita. Um pull request com três recusas bem justificadas vale mais que um com tudo aceito em silêncio.

Peso	O que é avaliado
25%	Qualidade da especificação: comportamento e não implementação, requisitos não funcionais com métrica
20%	Ambiguidades encontradas: lista separada, lacunas reais do enunciado
20%	Decisões justificadas: cada ambiguidade com decisão e razão
20%	Testes e código: um teste por critério, todos passando, testes antes do código no histórico
15%	Julgamento da revisão: cada item respondido, recusas justificadas
Duas coisas zeram o item correspondente: mexer no teste depois do código para fazê-lo passar, e aceitar a revisão em bloco sem responder item por item.

Se travar
Problema	O que fazer
O Copilot não sugere nada	Clique em Entrar, no canto inferior direito do editor, e autorize
ModuleNotFoundError: src	Rode python -m pytest -v a partir da raiz do projeto, não de dentro de uma pasta
Não acho onde criar o ramo	Canto inferior esquerdo do editor, onde está escrito main
Não acho onde fazer commit	Barra lateral esquerda, o ícone parecido com uma ramificação
Não aparece a tarja do pull request	Recarregue a página do seu repositório no GitHub depois do Publish Branch
Os testes passam rápido demais	Desconfie. Confira se o teste está mesmo verificando o critério, e não apenas rodando
O Codespace parou de responder	Recarregue a aba. Nada se perde: o que você salvou continua lá
O import demora ou parece travado	É normal levar um ou dois minutos. Recarregue a página do seu perfil e veja se o repositório já apareceu
Comandos, caso você queira
python -m pytest -v          # roda todos os testes, um por linha
python -m pytest -k atraso   # roda só os testes com "atraso" no nome
