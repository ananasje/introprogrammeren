def select_positive_odd_positions(values: list[int]) -> list[int]:
    """
    >>> select_positive_odd_positions([5, 3, 0, -2, 8, 4])
    [3, 4]
    """ 
    nieuwelst = []
    for i in range(len(values)):
        if i % 2 != 0:
            if val