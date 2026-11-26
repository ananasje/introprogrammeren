def word_start_positions(s: str) -> list[int]:
    """
    >>> word_start_positions("ik eet taart")
    [0, 3, 7]
    >>> word_start_positions("ik")
    [0, 3, 7]
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