def word_start_positions(s: str) -> list[int]:
    """
    >>> word_start_positions("ik eet taart")
    [0, 3, 7]
    >>> word_start_positions("ikhebhunger")
    [0]
    >>> word_start_positions("")
    []
    >>> word_start_positions("wat")
    []
    """
    nieuwelst = []
    inwoord = False
    for i in range(len(s)):
        
        if s[i] != " ":
            if inwoord == False:
                nieuwelst.append(i)
                inwoord = True
            
        elif s[i] == " ":
            inwoord = False
            
    return nieuwelst