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


@pytest.mark.parametrize('price, tax_rate, discount, expected', [(100, 10, 10, 99.0),
                                                                 (100, 10, 0, 110.0),
                                                                 (100, 20, 50, 60.0)])
def test_calculate_tax_with_discount(price, tax_rate, discount, expected):
    assert calculate_tax(price, tax_rate, discount=discount) == expected


@pytest.mark.parametrize('price, tax_rate, discount, round_count, expected', [(100, 10, 10, 1, 99.0),
                                                                              (200, 10, 0, 2, 220.00),
                                                                              (333, 21, 53, 3, 189.377)])
def test_calculate_tax_round(price, tax_rate, discount, round_count, expected):
    assert calculate_tax(price, tax_rate, discount=discount, round_count=round_count) == expected

@pytest.mark.parametrize('price, tax_rate, discount, round_count, expected', [(100, 10, '11', 1, 99.0),
                                                                              ("200", 10, 0, 2, 220.00),
                                                                              (333, 21, [53], 3, 189.377)])
def test_calculate_tax_round(price, tax_rate, discount, round_count, expected):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount=discount, round_count=round_count)

def test_calculate_tax_kwargs():
    with pytest.raises(TypeError):
        assert calculate_tax(100, 100, 33, round_count=3)
