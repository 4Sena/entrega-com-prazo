# Cole aqui os seus criterios de aceitacao, no formato Dado / Quando / Entao,
# um por requisito, antes de pedir qualquer teste ao Copilot.
#
# Exemplo do formato:
#   RF-002
#   Dado um trabalho com prazo em 10/11 as 23h59
#   Quando o aluno entrega em 10/11 as 22h00
#   Entao a nota final e igual a nota integral

from src.nota import calcular_nota_final
