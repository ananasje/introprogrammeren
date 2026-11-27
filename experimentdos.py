def first_word(s: str) -> str:
    
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
    
    inwoord = False 
    nieuwelst = ""
    
    for teken in s:
        if teken != " ":
            nieuwelst += teken
            inwoord = True
            
        elif teken == " ":
            if inwoord == True:
                return nieuwelst
                
    return nieuwelst
                
                