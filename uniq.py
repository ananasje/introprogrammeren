
def uniq(lst: list[object]) -> list[object]:
    """
    
    >>> uniq([])
    []
    >>> uniq([1, 2, 3])
    [1, 2, 3]
    
    """
    
    nieuwe_lijst = []

    for pos in range(len(lst)):
        if lst[pos] not in nieuwe_lijst:
            nieuwe_lijst.append(lst[pos])

    return nieuwe_lijst
