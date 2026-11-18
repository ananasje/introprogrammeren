def count_repeated_letters(words: list[str]) -> int:
    """
    >>> count_repeated_letters(["appel", "kat", "banana"])
    2
    >>> count_repeated_letters(["abc", "aabb", "xyz"])
    1
    >>> count_repeated_letters(["hello", "world", "test"])
    2
    >>> count_repeated_letters([])
    0
    """
    teller = 0
    alphabet = "azertyuiopqsdfghjklmwxcvbn"
    herhaling = ""
    for word in words:
        for teken in word:
            if teken in alpabet:
                herhaling.append(teken)
                
            if teken in herhaling:
                teller += 1
        
            
        
        
        
        