def word_start_positions(s: str) -> list[int]:
    """
    >>> word_start_positions("ik eet taart")
    [0, 3, 7]
    """
    nieuwelst = []
    for i in range(len(s)):
        
        inwoord = False
        
        if teken != "":
            if inwoord == False:
                nieuwelst.append(i)
                inwoord = True
            
        elif teken == "":
            