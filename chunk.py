def chunk(lst: list[int], n: int) -> list:
    resultaat = []
    groep = []
    for element in lst:
        groep.append(element)
        if len(groep) == n:
            resultaat.append(groep)
            groep = []
        