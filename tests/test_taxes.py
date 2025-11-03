import pytest
from src.funcs import calculate_taxes
from src.funcs import calculate_tax


@pytest.fixture
def prices():
    return [100, 200, 300]


@pytest.mark.parametrize('tax_rate, expected', [(10,[110, 220, 330]),
                                                (20,[120, 240, 360]),
                                                (30,[130, 260, 390])])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate():
    with pytest.raises(ValueError):
        calculate_taxes([110, 220, 330], -10)

def test_calculate_taxes_invalid_price():
    with pytest.raises(ValueError):
        calculate_taxes([0, -20], 33)

@pytest.mark.parametrize('price, tax_rate, expected', [(100, 10, 110.0), (50, 5, 52.5)])
def test_calculate_tax(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected

def test_calculate_tax_invalid_price():
    with pytest.raises(ValueError):
        calculate_tax(-100, 20)

def test_calculate_tax_invalid_tax_rate():
    with pytest.raises(ValueError) as exc:
        calculate_tax(100, -5)
    assert str(exc.value) == 'Неверный налоговый процент'

def test_calculate_tax_invalid_tax_rate():
    with pytest.raises(ValueError) as exc:
        calculate_tax(100, 100)





