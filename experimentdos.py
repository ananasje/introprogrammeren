def longest_even_streak(lst: list[int]) -> int:
    """
    >>> longest_even_streak([1, 2, 4, 6, 3, 8, 10])
    3
    >>> longest_even_streak([2, 4, 1, 6, 8, 10, 12])
    4
    >>> longest_even_streak([1, 3, 5])
    0
    >>> longest_even_streak([2, 4, 6])
    3
    >>> longest_even_streak([])
    0
    """
    langste = 0
    aantal = 0
    for teken in lst:
        if teken % 2 == 0:
            aantal += 1
        
        elif teken % 2 != 0:
            aantal == langste
            aantal = 0
    return langste
            
        
        
        
        