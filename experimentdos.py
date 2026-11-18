def count_long_words(s: str) -> int:
    """
    >>> count_long_words("kat olifant hond")
    2
    >>> count_long_words("  appel   peer ")
    2
    >>> count_long_words("Python")
    1
    >>> count_long_words("")
    0
    >>> count_long_words("a bb ccc")
    0
    """
    huidige_lengte = 0
    aantal = 0

    for teken in s:
        if teken == " ":
            huidige_lengte >= 0
            aantal =+ 1
            
        else:
            aantal += 0
        
        if huidige_lengte >= 4:
            aantal + 1
        
    return aantal