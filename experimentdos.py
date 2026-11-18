def merge_alternating(a: list[int], b: list[int]) -> list[int]:
    """
    >>> merge_alternating([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge_alternating([1, 2, 3], [9])
    [1, 9, 2, 3]
    >>> merge_alternating([], [4, 5])
    [4, 5]
    """
    new_list = []
    i = 0
    J = 0
    
    while i < len(a) and j < len(b):
        new_list.append(i)
        new_list.append(j)
        i =+ 1
        i =+ 1
        
        
        
        