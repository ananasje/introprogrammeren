def first_word(s: str) -> str:
    """
    >>> first_word("ik eet taart")
    'ik'
    >>> first_word("   appel en peer")
    'appel'
    >>> first_word("Python")
    'Python'
    >>> first_word("   ")
    ''
    """
    inwoord = False 
    nieuwelst = ""
    
    for teken in s:
        if teken != " ":
            nieuwelst += teken
            inwoord = True
        elif teken == " ":
            if inwoord == nieuwelst:
                nieuwelst = nieuwelst
    return nieuwelst
                
                