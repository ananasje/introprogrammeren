def longest_word_length(sentence: str) -> int:
    """
    >>> longest_word_length("ik eet een boterham")
    9
    >>> longest_word_length("kuwalis")
    7
    >>> longest_word_length("wortel of sap")
    6
    """
    langstewoord = 0
    huidigewoord = 0
    teller = 0
    for teken in sentence:
        if teken != " ":
            teller += 1
        
    if teken == " ":
        huidige woord
        if huidigewoord > langstewoord:
                langstewoord = huidigewoord
    
    return langstewoord
                
                
                
            