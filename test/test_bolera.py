from src.bolera import Bolera

def test_bolera():
    assert 60 == Bolera("12345123451234512345").calcular_puntos()
    assert 90 == Bolera("9-9-9-9-9-9-9-9-9-9-").calcular_puntos()
    assert 150 == Bolera('5/5/5/5/5/5/5/5/5/5/5').calcular_puntos()
    assert 141 == Bolera('XXX9-9-9-9-9-9-9-').calcular_puntos()
    assert 111 == Bolera('9-9-9-9-9-9-9-9-9-XXX').calcular_puntos()
    assert 149 == Bolera('8/549-XX5/53639/9/X').calcular_puntos()
    assert 175 == Bolera('X5/X5/XX5/--5/X5/').calcular_puntos()
    assert 120 == Bolera('XX9-9-9-9-9-9-9-9-').calcular_puntos()
