def count_words_with_digit(words: list[str]) -> int:
    """
    >>> count_words_with_digit(["abc", "a1b", "123"])
    2
    >>> count_words_with_digit(["kat", "hond"])
    0
    >>> count_words_with_digit([])
    0
    """
    count = 0
    
    for woord in words:
        heeft_cijfer = False
        for teken in woord:
            
            if teken.isdigit():
                heeft_cijfer = True
            
        if heeft_cijfer
                count += 1
    return count