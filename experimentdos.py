def count_even_groups(lst: list[int]) -> int:
    """
    >>> count_even_groups([2, 4, 1, 6, 8, 3, 10])
    3
    >>> count_even_groups([2, 4, 6])
    1
    >>> count_even_groups([1, 3, 5])
    0
    >>> count_even_groups([])
    0
    """
    teller = 0
    in_groep = False
    
    for teken in lst:
        if not in_groep:
                if teken % 2 == 0:
                teller += 1 
                in_groep = True
                
            
            
            