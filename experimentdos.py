def select_positive_odd_positions(values: list[int]) -> list[int]:
    """
    >>> select_positive_odd_positions([5, 3, 0, -2, 8, 4])
    [3, 4]
    >>> select_positive_odd_positions([])
    []
    >>> select_positive_odd_positions([3, 5, 7, 11])
    [5, 11]
    >>> select_positive_odd_positions([-3, -5, -7, -11])
    []
    
    """ 
    nieuwelst = []
    
    for i in range(len(values)):
        if i % 2 != 0:
            if values[i] >= 0:
                nieuwelst.append(values[i])
        
    return nieuwelst
        
def count_double_letter_words(words: list[str]) -> int:
    """
    >>> count_double_letter_words(["kat", "appel", "zee", "boom"])
    3
    >>> count_double_letter_words(["kat", "appel", "zee", "boom"])
    3
    """
    """
    teller = 0
    for woord in words:
        
        for i in range(1, len(woord)):
            if woord[i] == woord[i - 1]:
                teller += 1
    
    return teller