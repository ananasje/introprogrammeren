def hoeveelheid_water(minuten: int) -> int:
    """
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.

    >>> hoeveelheid_water(1)
    12
    >>> hoeveelheid_water(10)
    120
    >>> hoeveelheid_water(5)
    60
    >>> hoeveelheid_water(0)
    0
    """
    flesjes = minuten * 12
    return flesjes


if __name__ == '__main__':
    minuten = int(input("Hoeveel minuten douche je? "))
    resultaat = hoeveelheid_water(minuten)
    print(resultaat)