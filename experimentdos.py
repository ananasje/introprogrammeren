def count_repeats(words: list[str]) -> int:
    """
    >>> count_repeats(["kat", "kat", "vis", "vis", "vis"])
    3
    >>> count_repeats(["kat", "Kat"])
    3
    """
    teller = 0
    
    for i in range  (1,len(words)):
        if words[i] == words[i - 1]:
            teller += 1
    return teller