from multiprocessing.managers import Value


def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price: float,
                  tax_rate: float,
                  discount: float = 0,
                  round_count: int = 2) -> float:
    for arg in [price, tax_rate, discount]:
        if isinstance(arg, float) == False and isinstance(arg, int) == False:
            raise TypeError('Ошибка типа данных')
        if not isinstance(round_count, int):
            raise TypeError('Ошибка типа данных')
    if price <= 0:
        raise ValueError('Неверная цена')
    if not 0 < tax_rate < 100:
        raise ValueError('Неверный налоговый процент')
    result = (price * (100 + tax_rate) / 100) * (100 - discount) / 100
    return round(result, round_count)

