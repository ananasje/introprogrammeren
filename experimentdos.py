def get_positive(lst: list[int]) -> list[int]:
    """
    >>> get_positive([-2, 4, 0, 7])
    [4, 7]
    >>> get_positive([-3, -1])
    []
    >>> get_positive([])
    []
    """
    new_list = []
    i = 0
    while i < len(lst):
        if lst[i] > 0:
            new_list.append(lst[i])
    
    i += 1