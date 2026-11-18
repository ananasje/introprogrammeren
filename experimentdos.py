def remove_duplicates(lst: list[int]) -> list[int]:
    """
    >>> remove_duplicates([3, 1, 3, 2, 1])
    [3, 1, 2]
    >>> remove_duplicates([5, 5, 5])
    [5]
    >>> remove_duplicates([4, 2, 7])
    [4, 2, 7]
    >>> remove_duplicates([])
    []
    """
    
    nieuwe_lijst = []
    
    for teken in lst:
        if teken not in nieuwe_lijst:
            nieuwe_lijst.append(teken)
            
            
            