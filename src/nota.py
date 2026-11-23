import math
from datetime import datetime, timedelta


def calcular_nota_final(nota, prazo, entrega, justificativa_aprovada, novo_prazo):
    """Calcula a nota final de uma entrega, aplicando a regra de atraso."""
    if not isinstance(nota, (int, float)) or isinstance(nota, bool):
        raise ValueError("nota deve ser numérica")
    if not math.isfinite(nota) or nota < 0 or nota > 10:
        raise ValueError("nota deve estar entre 0 e 10")

    for nome, data in (("prazo", prazo), ("entrega", entrega)):
        if not isinstance(data, datetime):
            raise ValueError(f"{nome} deve ser datetime")

    if not isinstance(justificativa_aprovada, bool):
        raise ValueError("justificativa_aprovada deve ser booleana")

    if justificativa_aprovada:
        if not isinstance(novo_prazo, datetime):
            raise ValueError("novo_prazo deve ser datetime")
    elif novo_prazo is not None:
        if not isinstance(novo_prazo, datetime):
            raise ValueError("novo_prazo deve ser datetime")

    if novo_prazo is not None and novo_prazo < prazo:
        raise ValueError("novo_prazo não pode ser anterior ao prazo")

    prazo_para_calculo = novo_prazo if justificativa_aprovada else prazo

    atraso = entrega - prazo_para_calculo
    if atraso <= timedelta(0):
        dias_atraso = 0
    else:
        micros_por_dia = 24 * 60 * 60 * 1_000_000
        micros_atraso = atraso // timedelta(microseconds=1)
        dias_atraso = (micros_atraso + micros_por_dia - 1) // micros_por_dia

    desconto_percentual = min(dias_atraso * 10, 50)
    aceita = dias_atraso <= 5

    if not aceita:
        nota_final = None
    else:
        nota_final = round(nota * (1 - desconto_percentual / 100), 2)

    return {
        "nota_final": nota_final,
        "desconto_percentual": desconto_percentual,
        "dias_atraso": dias_atraso,
        "aceita": aceita,
    }
