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
    
    for i in s:
        if i != " ":
            nieuwelst += teken
            inwoord = True
        else:
            if inwoord == False:
                
                