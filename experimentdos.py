def longest_word_length(sentence: str) -> int:
    """
    >>> longest_word_length("ik eet een boterham")
    9
    >>> longest_word_length("kuwalis")
    7
    """
    langstewoord = 0
    huidigewoord = 0
    teller = 0
    for teken in sentence:
        if teken != " ":
            huidigewoord += 1
        
    else:
            if huidigewoord > langstewoord:
                langstewoord = huidigewoord
    
    return langstewoord
                
                
                
            