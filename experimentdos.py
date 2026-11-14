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
        for teken in woord:
            
            if teken in "1234567890" > 1:
            count += 1
        else:
            count == 0
    return count