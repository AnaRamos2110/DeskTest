import funcao_pytest

def test_soma():
    assert funcao_pytest.soma(2, 3) == 5
    assert funcao_pytest.soma(1, -1) == 0

    #'macete' do pytest: você só chama o interpretador dentro do terminal ! Comando --  python -m pytest test_pytest.py