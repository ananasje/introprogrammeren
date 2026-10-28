def travel_costs(km: int) -> float:
    """
    Bepaalt de vervoerskosten voor de heen- en terugreis.

    >>> travel_costs(100)
    26.0
    >>> travel_costs(800)
    208.0
    """
    return km * 2 * 0.13


def overnight_costs(nights: int) -> float:
    """
    Bepaalt de overnachtingskosten.

    >>> overnight_costs(5)
    300.0
    >>> overnight_costs(10)
    600.0
    """
    return nights * 60.0


def total_costs(km: int, nights: int) -> int:
    """
    Bepaalt de totale vakantiekosten en rondt af.

    >>> total_costs(1250, 5)
    625
    >>> total_costs(800, 10)
    808
    >>> total_costs(2159, 12)
    1281
    """
    vervoer = travel_costs(km)
    verblijf = overnight_costs(nights)
    totaal = vervoer + verblijf
    return int(totaal + 0.5)


if __name__ == '__main__':
    km = int(input("Hoe ver ga je weg in kilometers? "))
    nights = int(input("Hoe veel nachten is je verblijf? "))

    resultaat = total_costs(km, nights)
    print(f"Jouw vakantie kost: {resultaat}")