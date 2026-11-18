def selection_sort(lst: list[int]) -> list[int]:
    """
    >>> selection_sort([7, 4, 2, 6])
    [2, 4, 6, 7]
    >>> selection_sort([5, 1, 5, 2])
    [1, 2, 5, 5]
    >>> selection_sort([])
    []
    """
    
    kleinste_pos = 0
    
            