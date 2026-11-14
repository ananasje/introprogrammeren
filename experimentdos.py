def count_words_with_digit(words: list[str]) -> int:
    """
    >>> count_words_with_digit(["abc", "a1b", "123"])
    2
    >>> count_words_with_digit(["kat", "hond"])
    0
    >>> count_words_with_digit([])
    0
    """
    teller = 0
    
    for teken in words:
        if teken in "1234567890":
            count += 1
            
    return count