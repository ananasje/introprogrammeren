def digit_group_starts(s: str) -> list[int]:
    """
    >>> digit_group_starts("ab12c003x8")
    [2, 5, 9]
    """
    nieuwlist = []
    group = False
    for teken in s:
        if teken.isdigit():
            if group == False:
                nieuwlist.append(tekeni)
                group = True
        else:
            group = False
    
    return nieuwlist
            
            
                
            