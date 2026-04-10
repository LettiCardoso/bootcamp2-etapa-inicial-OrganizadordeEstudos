import pytest
from src.logic import SessaoDeEstudo 

def test_session_criacao():
    session = SessaoDeEstudo("Matemática", 25)
    assert session.nome == "Matemática"
    assert session.duracao_minutos == 1500

def test_invalid_task_name():
    with pytest.raises(ValueError):
        SessaoDeEstudo("", 25)

def test_time_formatting():
    session = SessaoDeEstudo("Teste", 10)
    assert session.get_duracao_string(125) == "02:05"