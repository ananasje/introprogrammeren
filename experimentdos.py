def get_smaller(lst: list[int]) -> list[int]:
    """
    >>> get_smaller([8, 3, 5, 2, 1])
    [3, 2, 1]
    >>> get_smaller([1, 2, 3])
    []
    >>> get_smaller([4, 4, 2])
    [2]
    >>> get_smaller([])
    []
    """
    nieuwe_lijst = []
    
    for pos in range(1, len(lst)):
        if lst[pos < lst[pos - 1]:
            nieuwe_lijst.append(lst[pos])
        
    return nieuwe_lijst
        
        