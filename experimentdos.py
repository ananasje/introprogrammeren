def count_vowely_words(s: str) -> int:
    """
    >>> count_vowely_words("de groene kamer")
    2
    >>> count_vowely_words("auto fiets kat")
    2
    >>> count_vowely_words("boom")
    1
    >>> count_vowely_words("")
    0
    """
    klinker = "aeiou"
    teller = 0
    klinkerteller = 0
    for word in s:
        for teken in word:
            if teken != " ":
                if teken in klinker:
                    klinkerteller += 1
                    
            if teken == " "
                    if klinkerteller >= 2
                    teller =+ 1
                    klinkerteller =  0
        
            
    
    