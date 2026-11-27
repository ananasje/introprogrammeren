def last_digit_position(s: str) -> str:
    """
    >>> mask_first_digit("abc123")
    'abc#23'
    >>> mask_first_digit("7dagen9")
    '#dagen9'
    >>> mask_first_digit("hallo")
    'hallo'
    >>> mask_first_digit("")
    ''
    """
    nieuwestr = ""
    al_vervangen = False
    for i in range(len(s)):
        
        if s[i].isdigit() and al_vervangen == False:
            nieuwestr += "#"
            al_vervangen = True
        else:
            nieuwestr =  s[i]
            
    return nieuwestr
    
            