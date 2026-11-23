def digit_group_starts(s: str) -> list[int]:
    """
    >>> digit_group_starts("ab12c003x8")
    [2, 5, 9]
    """
    nieuwlist = []
    group = False
    for i in s:
        if s[i].isdigit():
            if group == False:
                nieuwlist.append(i)
            
            
                
            