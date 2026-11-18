def count_negative_groups(lst: list[int]) -> int:
    """
    >>> count_negative_groups([-2, -5, 3, -1, -4, 0, -7])
    3
    >>> count_negative_groups([-1, -2, -3])
    1
    >>> count_negative_groups([1, 2, 3])
    0
    >>> count_negative_groups([])
    0
    """
    teller = 0
    in_groep = False
    
    for teken in lst:
        if teken < 0:
            if not in_groep:
                teller += 1
                in_groep = True
        else:
            teken
            