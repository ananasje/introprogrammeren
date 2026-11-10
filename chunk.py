def chunk(lst: list[int], n: int) -> list:
    resultaat = []
    groep = []
    groep2 = []
groep = []

for element in lst:
    groep.append(element)

    if len(groep) == n: