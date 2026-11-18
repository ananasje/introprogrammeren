def longest_even_streak(lst: list[int]) -> int:
    """
    >>> longest_even_streak([2, 4, 6, 3, 8, 10])
    3
    >>> longest_even_streak([1, 3, 5])
    0
    >>> longest_even_streak([2, 4, 1, 6, 8, 10, 12])
    4
    >>> longest_even_streak([])
    0
    """
    
    teller = 0
    langste = 0
    for pos in range (1,len(lst) - 1):
        if lst[pos] % 2 == 0:
            teller + 1
    if lst[pos + 1] % 2 = 0: