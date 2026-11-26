def first_word(s: str) -> str:
    """
    >>> first_word("ik eet taart")
    'ik'
    >>> first_word("   appel en peer")
    'appel'
    """
    nieuwestring = ""
    ineerstewoord = False
    for teken in s:
        if teken != " ":
            if ineerstewoord == False:
                nieuwestring += teken
                
                
        elif teken == " "
            ineerstewoord = True
    return nieuwestring