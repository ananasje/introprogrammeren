def count_direction_changes(values: list[int]) -> int:
    """
    >>> count_direction_changes([2, 7, 3, 9, 4])
    2
    >>> count_direction_changes([3, 3, 3, 3, 3])
    0
    >>> count_direction_changes([3, 3, 3, 3, 3])
    0
    """
    teller = 0
    for i in range(1,(len(values)) -1):
        if len(values) > 3:
            if values[i] > values[i - 1] and values[i] > values[i + 1]:
                teller += 1
        
    return teller