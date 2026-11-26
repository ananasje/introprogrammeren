def first_word(s: str) -> str:
    """
    >>> first_word("ik eet taart")
    'ik'
    >>> first_word("   appel")
    'appel'
    """
    
    nieuwestring = ""
    ineerstewoord = False
    
    for teken in s:
        if teken != " ":
                nieuwestring += teken
                ineerstewoord = True
                
        elif ineerstewoord:
            return nieuwestring
            
    return nieuwestring
    