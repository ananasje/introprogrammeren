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
    tekenteller = 0
    alphabet = "azertyuiopqsdfghjklmwxcvbn"
    herhaling = ""
    for word in words:
        for teken in word:
            if teken in alphabet:
                herhaling.append(teken)
                
            if teken in herhaling:
                tekenteller += 1
        
    return tekenteller
    
def count_repeated_letters(words: list[str]) -> int:
    tekenteller = 0

    for word in words:
        gezien = ""
        heeft_herhaling = False

        for teken in word:
            if teken in gezien:
                heeft_herhaling = True
            else:
                gezien += teken

        if heeft_herhaling:
            tekenteller += 1

    return tekenteller
        
        
        