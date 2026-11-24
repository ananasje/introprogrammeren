def first_negative(values: list[int]) -> int:
    """
    >>> first_negative([5, 3, -7, 2, -1])
    2
    >>> first_negative([4, 8, 9])
    -1
    
    """
    antwoord = 0

    for i in range(len(values)):
        if values[i] < 0:
            antwoord += i
            
            
            return antwoord
        elif values[i] > 0:
            antwoord += -1
            
            return antwoord