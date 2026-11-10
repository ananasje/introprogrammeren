def chunk(lst: list[int], n: int) -> list[list[int]]:
    
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
