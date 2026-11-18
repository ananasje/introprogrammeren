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
            teller >= 4
            lange_woord +=1
    
            