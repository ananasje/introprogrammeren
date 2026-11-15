def merge_alternating(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    >>> merge_alternating([1, 2, 3], [8, 9])
    [1, 8, 2, 9, 3]

    >>> merge_alternating([1, 2], [7, 8, 9])
    [1, 7, 2, 8, 9]

    >>> merge_alternating([1, 2], [3, 4])
    [1, 3, 2, 4]

    >>> merge_alternating([], [5, 6])
    [5, 6]

    >>> merge_alternating([], [])
    []
    """
    nieuwe_lijst = []
    i = 0
    j = 0
    while i < len(lst1) and  j < len(lst2):
        nieuwe_lijst.append(i)