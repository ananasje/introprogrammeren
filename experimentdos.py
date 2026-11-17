def count_words(s: str) -> int:
    """
    >>> count_words("Ik leer Python")
    3
    >>> count_words("Hallo")
    1
    >>> count_words("  kat   hond  ")
    2
    >>> count_words("")
    0
    >>> count_words("   ")
    0
    """
    teller = 0 
    in_woord = false 
    
    for teken in s:
        if char != " " and not in_woord:
            teller += 1
        elif teken = " ":
            
            in_woord = false 
    
    return teller 
        
        