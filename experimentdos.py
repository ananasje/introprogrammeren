def filter_long_even_words(words: list[str]) -> list[str]:
    
    """
    >>> filter_long_even_words(["appel", "fiets", "auto", "kat"])
    ["fiets", "auto"]
    >>> filter_long_even_words(["boek", "peer", "boom"])
    ["boek", "peer"]
    >>> filter_long_even_words(["xyz", "aaaa", "huis"])
    ["aaaa", "huis"]
    >>> filter_long_even_words([])
    []
    """
    nieuwelijst = []
    klinker = "aeiouAEIOU"
    
    for word in words:
        for teken in word:
                if teken in klinker:
                    klinkerteller += 1
        
        if len(word) >= 4 and klinkerteller > 1 and klinkerteller % 2 == 0:
            nieuwelijst.append(word)
            
    return nieuwelijst
             
            
    
    