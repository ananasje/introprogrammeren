def get_decreases(lst: list[int]) -> list[int]:
    """
    >>> get_decreases([5, 3, 7, 2, 1])
    [3, 2, 1]
    >>> get_decreases([1, 2, 3])
    []
    >>> get_decreases([4, 4, 2])
    [2]
    """
    nieuwe_lijst = []
    for pos in range(1, len(lst)):
        if lst[pos] < lst[pos - 1]:
            nieuwe_lijst.append()
    