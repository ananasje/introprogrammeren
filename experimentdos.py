def mask_digits(s: str) -> str:
    """
    >>> mask_digits("Mijn code is 1234!")
    'Mijn code is ####!'
    >>> mask_digits("123456781234567")
    '###############'
    >>> mask_digits("is dit roblox??")
    'is dit roblox??'
    
    """
    nieuwestr = ""
    for teken in s:
        if teken.isdigit():
            nieuwestr += "#"
            
        else:
            nieuwestr += teken
            
    return nieuwestr
        