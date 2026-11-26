def mask_digits(s: str) -> str:
    """
    >>> mask_digits("Mijn code is 1234!")
    'Mijn code is ####!'
    """
    nieuwestr = ""
    for teken in s:
        if teken.isdigit():
            nieuwestr += "#"
            
        else:
            ni
        