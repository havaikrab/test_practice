import pytest
from src.funcs import calculate_taxes


@pytest.fixture
def prices():
    return [100, 200, 300]


@pytest.mark.parametrize('tax_rate, expected', [(10,[110, 220, 330]),
                                                (20,[120, 240, 360]),
                                                (30,[130, 260, 390])])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([110, 220, 330], -10)
    assert str(exc_info.value) == 'Неверный налоговый процент'

def test_calculate_taxes_invalid_price():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([0, -20], 33)
    assert str(exc_info.value) == 'Неверная цена'
