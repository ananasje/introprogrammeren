def count_direction_changes(values: list[int]) -> int:
    """
    >>> count_direction_changes([2, 7, 3, 9, 4])
    2
    """
    teller = 0
    for i in range(len(values)):
        if values(i)