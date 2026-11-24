def first_zero(values: list[int]) -> int:
    """
    >>> first_zero([8, 3, 0, 4, 0])
    2
    >>> first_zero([])
    -1
    >>> first_zero([3, 6, 9])
    -1
    >>> first_zero([0, 8, 12)
    0
    """
    i = 0

    while i < len(values):
        if values[i] == 0:
            return i

        i += 1

    return -1   
        
            