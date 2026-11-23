def count_direction_changes(values: list[int]) -> int:
    """
    >>> count_direction_changes([2, 7, 3, 9, 4])
    2
    """
    teller = 0
    for i in range(len(values)):
        if len(values) < 3:
        if values[i] < values[i - 1] and values[i] < values[i + 1]:
            teller += 1
            
    return teller