def count_even_positions(values: list[int]) -> int:
    """
    >>> count_even_positions([4, 7, 6, 8, 10])
    3
    >>> count_even_positions([4, 7, 6, 8, 10])
    3
    """
    teller = 0
    for i in range(len(values)):
        if i % 2 == 0:
            if values[i] % 2 == 0:
                teller += 1
    
    return teller