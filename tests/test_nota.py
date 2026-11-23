# CA1 (RF1). Dado nota 8,0 e prazo 20/11 23:59, quando a entrega ocorre às 23:59 em ponto, então nota_final = 8,0, desconto_percentual = 0, dias_atraso = 0 e aceita = True.

# CA2 (RF2). Dado nota 10 e prazo 20/11 23:59, quando a entrega ocorre 1 segundo depois, então dias_atraso = 1, desconto_percentual = 10 e nota_final = 9,0. Quando a entrega ocorre 25h depois, então dias_atraso = 2 e nota_final = 8,0.

# CA3 (RF3). Dado nota 10, quando a entrega ocorre com exatamente 5 dias de atraso (120h), então desconto_percentual = 50, nota_final = 5,0 e aceita = True.

# CA4 (RF4). Dado nota 10, quando a entrega ocorre 120h e 1 segundo depois do prazo, então aceita = False e nota_final = None.

# CA5 (RF5). Dado justificativa aprovada com novo prazo 25/11 23:59, quando a entrega ocorre em 24/11 (depois do prazo original), então desconto_percentual = 0, dias_atraso = 0 e nota_final = nota integral.

# CA6 (RF6). Dado justificativa aprovada com novo prazo 25/11 23:59, quando a entrega ocorre 1 segundo depois do novo prazo, então dias_atraso = 1 e desconto_percentual = 10.

# CA7 (RF7). Dado qualquer entrada válida, quando a função é chamada, então o retorno é um dicionário com exatamente as chaves nota_final, desconto_percentual, dias_atraso e aceita.

# CA8 (RF8). Dado nota 11, ou nota -1, ou justificativa aprovada sem novo_prazo, ou novo_prazo anterior ao prazo, quando a função é chamada, então levanta ValueError.

# CA9 (RF9). Dado nota 6,66 e 1 dia de atraso, quando a função é chamada, então nota_final = 5,99 (5,994 arredondado para 2 casas).

from src.nota import calcular_nota_final

from datetime import datetime, timedelta

import pytest


def test_ca1_entrega_no_prazo_exato():
    prazo = datetime(2026, 11, 20, 23, 59)
    entrega = datetime(2026, 11, 20, 23, 59)

    resultado = calcular_nota_final(8.0, prazo, entrega, False, None)

    assert resultado == {
        "nota_final": 8.0,
        "desconto_percentual": 0,
        "dias_atraso": 0,
        "aceita": True,
    }


def test_ca2_atraso_de_um_segundo_e_vinte_e_cinco_horas():
    prazo = datetime(2026, 11, 20, 23, 59)

    resultado_um_segundo = calcular_nota_final(
        10,
        prazo,
        prazo + timedelta(seconds=1),
        False,
        None,
    )
    resultado_vinte_cinco_horas = calcular_nota_final(
        10,
        prazo,
        prazo + timedelta(hours=25),
        False,
        None,
    )

    assert resultado_um_segundo["dias_atraso"] == 1
    assert resultado_um_segundo["desconto_percentual"] == 10
    assert resultado_um_segundo["nota_final"] == 9.0
    assert resultado_vinte_cinco_horas["dias_atraso"] == 2
    assert resultado_vinte_cinco_horas["nota_final"] == 8.0


def test_ca3_atraso_exatamente_cinco_dias():
    prazo = datetime(2026, 11, 20, 23, 59)

    resultado = calcular_nota_final(
        10,
        prazo,
        prazo + timedelta(hours=120),
        False,
        None,
    )

    assert resultado["desconto_percentual"] == 50
    assert resultado["nota_final"] == 5.0
    assert resultado["aceita"] is True


def test_ca4_atraso_maior_que_cinco_dias():
    prazo = datetime(2026, 11, 20, 23, 59)

    resultado = calcular_nota_final(
        10,
        prazo,
        prazo + timedelta(hours=120, seconds=1),
        False,
        None,
    )

    assert resultado["aceita"] is False
    assert resultado["nota_final"] is None


def test_ca5_justificativa_aprovada_entrega_apos_prazo_original():
    prazo = datetime(2026, 11, 20, 23, 59)
    novo_prazo = datetime(2026, 11, 25, 23, 59)

    resultado = calcular_nota_final(
        10,
        prazo,
        datetime(2026, 11, 24),
        True,
        novo_prazo,
    )

    assert resultado["desconto_percentual"] == 0
    assert resultado["dias_atraso"] == 0
    assert resultado["nota_final"] == 10


def test_ca6_justificativa_aprovada_atraso_um_segundo_no_novo_prazo():
    prazo = datetime(2026, 11, 20, 23, 59)
    novo_prazo = datetime(2026, 11, 25, 23, 59)

    resultado = calcular_nota_final(
        10,
        prazo,
        novo_prazo + timedelta(seconds=1),
        True,
        novo_prazo,
    )

    assert resultado["dias_atraso"] == 1
    assert resultado["desconto_percentual"] == 10


def test_ca7_retorno_tem_exatamente_as_chaves_exigidas():
    prazo = datetime(2026, 11, 20, 23, 59)

    resultado = calcular_nota_final(
        8,
        prazo,
        datetime(2026, 11, 21),
        False,
        None,
    )

    assert set(resultado.keys()) == {
        "nota_final",
        "desconto_percentual",
        "dias_atraso",
        "aceita",
    }


@pytest.mark.parametrize(
    ("nota", "prazo", "justificativa_aprovada", "novo_prazo"),
    [
        (11, datetime(2026, 11, 20, 23, 59), False, None),
        (-1, datetime(2026, 11, 20, 23, 59), False, None),
        (
            10,
            datetime(2026, 11, 20, 23, 59),
            True,
            None,
        ),
        (
            10,
            datetime(2026, 11, 20, 23, 59),
            True,
            datetime(2026, 11, 19, 23, 59),
        ),
    ],
)
def test_ca8_entradas_invalidas(
    nota,
    prazo,
    justificativa_aprovada,
    novo_prazo,
):
    with pytest.raises(ValueError):
        calcular_nota_final(
            nota,
            prazo,
            prazo,
            justificativa_aprovada,
            novo_prazo,
        )


def test_ca9_arredondamento_da_nota_final():
    prazo = datetime(2026, 11, 20, 23, 59)

    resultado = calcular_nota_final(
        6.66,
        prazo,
        prazo + timedelta(days=1),
        False,
        None,
    )

    assert resultado["nota_final"] == 5.99
