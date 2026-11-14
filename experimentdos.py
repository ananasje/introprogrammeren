def same_positions(lst1: list[int], lst2: list[int]) -> int:
    """
    >>> same_positions([1, 2, 3], [1, 5, 3])
    2
    >>> same_positions([4, 5, 6], [1, 2, 3])
    0
    >>> same_positions([7, 8], [7, 8])
    2
    >>> same_positions([], [])
    0
    """
    count = 0
    for pos in lst1 and lst2:
        if pos[lst1] - pos[lst2]
        