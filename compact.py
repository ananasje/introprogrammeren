
def compact(lst: list[object]) -> list[object]:
    """
    Maakt een nieuwe lijst zonder falsy elementen.
    De oorspronkelijke lijst blijft onveranderd.

    >>> compact([1, 0, 2, 0, 3])
    [1, 2, 3]
    >>> compact(["hallo", "", "wereld"])
    ['hallo', 'wereld']
    >>> compact([False, True, None, 5])
    [True, 5]
    >>> compact([0, "", None, False])
    []
    >>> compact([])
    []
    >>> compact([1, 2, 3])
    [1, 2, 3]
    >>> origineel = [0, 1, "", 2]
    >>> compact(origineel)
    [1, 2]
    >>> origineel
    [0, 1, '', 2]
    """
    nieuwe_lijst = []

    for item in lst:
        if item:
            nieuwe_lijst.append(item)

    return nieuwe_lijst
