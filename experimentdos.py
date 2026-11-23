def first_negative(values: list[int]) -> int:
    """
    >>> first_negative([5, 3, -7, 2, -1])
    2
    >>> first_negative([4, 8, 9])
    -1
    
    """
    antwoord = 0
    for nummer in values:
        if nummer < 0:
        antwoord += nummer
        break 
    
    return nummer