def count_repeats(words: list[str]) -> int:
    """
    Schrijf precies vier doctests.
    """
    teller = 0
    
    for i in range  1,len(words)):
        if words[i] == words[i]:
            teller += 1
    return teller