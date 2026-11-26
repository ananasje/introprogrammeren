def count_words(s: str) -> int:
    """
    >>> count_words("ik   eet  taart")
    3
    >>> count_words("Ik BeN")
    2
    >>> count_words("ikBenTaarT")
    1
    >>> count_words("")
    0
    """
    teller = 0
    inwoord = False
    for teken in s:
        if teken != " ":
            if inwoord == False:
                teller += 1
                inwoord = True
        
        else:
            if teken == " ":
                inwoord = False
    
    return teller