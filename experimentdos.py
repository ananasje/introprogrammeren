def digit_group_starts(s: str) -> list[int]:
    """
    >>> digit_group_starts("ab12c003x8")
    [2, 5, 9]
    >>> digit_group_starts("")
    []
    >>> digit_group_starts("")
    []
    """
    nieuwlist = []
    group = False
    for i in range(len(s)):
        if s[i].isdigit():
            if group == False:
                nieuwlist.append(i)
                group = True
        else:
            group = False
    
    return nieuwlist
            
            
                
            