def chunk(lst: list[int], n: int) -> list[list[int]]:
    """
    >>>chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>>chunk([2, 6, 7], 2)
    [[1, 2], [3, 4], [5]]
    """
    resultaat = []
    groep = []

    for element in lst:
        groep.append(element)

        if len(groep) == n:
            resultaat.append(groep)
            groep = []

    if len(groep) > 0:
        resultaat.append(groep)

    return resultaat
