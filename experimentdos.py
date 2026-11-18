def count_vowel_words(words: list[str]) -> int:
    """
    >>> count_vowel_words(["appel", "fiets", "kat"])
    2
    >>> count_vowel_words(["banana", "auto", "peer"])
    1
    >>> count_vowel_words(["boek", "huis", "xyz"])
    2
    >>> count_vowel_words([])
    0
    """
    
    klinkerteller = 0
    teller = 0
    for word in words:
        for teken in word:
            if teken == "a":
                klinkerteller += 1
            if teken == "a":
                klinkerteller += 1
        
        
        