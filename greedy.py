def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag cents kan worden teruggegeven.

    >>> count_coins(41)
    4
        >>> count_coins(73)
    7
    >>> count_coins(99)
    9
    >>> count_coins(30)
    2
    >>> count_coins(87)
    6
    >>> count_coins(124)
    8
    >>> count_coins(1)
    1
    >>> count_coins(0)
    0
    """
    coins = 0

    while cents >= 25:
        cents = cents - 25
        coins = coins + 1

    while cents >= 10:
        cents = cents - 10
        coins = coins + 1

    while cents >= 5:
        cents = cents - 5
        coins = coins + 1

    while cents >= 1:
        cents = cents - 1
        coins = coins + 1

    return coins


if __name__ == '__main__':
    amount = float(input("Hoeveel wisselgeld moet er gegeven worden? "))

    while amount < 0:
        amount = float(input("Hoeveel wisselgeld moet er gegeven worden? "))

    cents = int(round(amount * 100))
    result = count_coins(cents)
    print(result)