def last_word(s: str) -> str:
    
    """
    >>> last_word("ik eet taart")
    'taart'
    >>> last_word("  hallo wereld   ")
    'wereld'
    >>> last_word("Python")
    'Python'
    >>> last_word("   ")
    ''
    ''
    """
    huidigewoord = ""
    laatstewoord = ""
    inwoord = False
    
    for teken in s:
        if teken != " ":
            huidigewoord += teken
            inwoord = True
            
        elif teken == " ":
            if inwoord == True:
                

    return huidigewoord