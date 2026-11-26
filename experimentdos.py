def count_words(s: str) -> int:
    """
    >>> count_words("ik   eet  taart")
    3
    """
    teller = 0
    inwoord = False
    for teken in s:
        if teken != " ":
            if inwoord == False:
                teller += 1
                inwoord = True