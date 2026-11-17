def count_local_minima(lst: list[int]) -> int:
    """
    >>> count_local_minima([5, 2, 7, 1, 6])
    2
    >>> count_local_minima([1, 2, 3, 4])
    0
    >>> count_local_minima([4, 1, 4, 1, 4])
    2
    >>> count_local_minima([2, 2, 2])
    0
    >>> count_local_minima([])
    0
    """
    teller = 0
    for pos in range(1,len(lst)) - 1:
        if lst[pos] < lst[pos + 1] and lst[pos] < lst[pos - 1]:
            teller += 1
    
    return teller
        
        