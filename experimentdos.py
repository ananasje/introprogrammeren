def count_long_words(s: str) -> int:
    """
    >>> count_long_words("kat olifant fiets")
    2
    >>> count_long_words("  appel   peer  ")
    1
    >>> count_long_words("Python")
    1
    >>> count_long_words("")
    0
    >>> count_long_words("a bb ccc")
    0
    """
    lange_woord = 0
    teller = 0
    for teken in s:
        if teken != " ":
            teller += 1
            
        if teken == " ":
            teller >= 5
            lange_woord +=1
    
    return lange_woord

def get_local_maxima(lst: list[int]) -> list[int]:
    """
    >>> get_local_maxima([1, 5, 2, 8, 3])
    [5, 8]
    >>> get_local_maxima([1, 2, 3, 4])
    []
    >>> get_local_maxima([4, 4, 2])
    []
    >>> get_local_maxima([])
    []
    """
    nieuwe_lijst= []
    
    for pos in range (1,(len(lst)-1)):
        if lst[pos] > lst[pos -1] and lst[pos] > lst[pos +1]:
        nieuwe_lijst.append()
    
    
    
            