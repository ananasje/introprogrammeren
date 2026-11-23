def longest_word_length(sentence: str) -> int:
    """
    
    
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
                
                
                
            