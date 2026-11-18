def count_peaks(lst: list[int]) -> int:
    """
    >>> count_peaks([1, 5, 2, 8, 3])
    2
    >>> count_peaks([1, 2, 3, 4])
    0
    >>> count_peaks([3, 3, 3])
    0
    >>> count_peaks([5])
    0
    >>> count_peaks([])
    0
    """
    teller = 0
    
    for pos in range(1,len(lst)):
        if lst[pos] < lst[pos]
                