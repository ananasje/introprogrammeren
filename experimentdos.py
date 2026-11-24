def first_zero(values: list[int]) -> int:
    """
    >>> first_zero([8, 3, 0, 4, 0])
    2
    """
    i = 0
    resultaat = 0
    while i < len(values):
        if values[i] == 0:
            resultaat += i
        else: 
            i + 1
        
        
            