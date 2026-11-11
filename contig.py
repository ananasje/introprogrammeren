
def contig(lst: list[int]) -> list[list[int]]:
    """
    >>> contig([3, 4, 5, 9, 10])
    [[3, 4, 5], [9, 10]]
    >>> contig([1, 2, 7, 8, 12])
    [[1, 2], [7, 8], [12]]
    >>> contig([5])
    [[5]]
    >>> contig([])
    []
    >>> contig([3, 3, 4])
    [[3], [3, 4]]
    """
    nieuwe_lijst = []
    lege_lijst = []

    for pos in range(len(lst) - 1):
        lege_lijst.append(lst[pos])

        if lst[pos + 1] != lst[pos] + 1:
            nieuwe_lijst.append(lege_lijst)
            lege_lijst = []

    if len(lst) > 0:
        lege_lijst.append(lst[-1])
        nieuwe_lijst.append(lege_lijst)

    return nieuwe_lijst

