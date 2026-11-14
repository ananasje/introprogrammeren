def merge_sorted(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    >>> merge_sorted([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge_sorted([1, 2], [3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> merge_sorted([], [2, 4])
    [2, 4]
    >>> merge_sorted([1, 3], [1, 3])
    [1, 1, 3, 3]
    """
    
    nieuwe_lijst = []
    i = 0  #positie in lijst 1
    j = 0  #positie in lijst 2
    while i 