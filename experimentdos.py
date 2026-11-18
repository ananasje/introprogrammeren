def count_words_with_two_digits(words: list[str]) -> int:
    """
    >>> count_words_with_two_digits(["a12", "b3", "456"])
    2
    >>> count_words_with_two_digits(["abc", "a1b", "xyz"])
    0
    >>> count_words_with_two_digits(["12", "34", "a567b"])
    3
    >>> count_words_with_two_digits([])
    0
    """
    
    teller = 0
    
    for word in words:
        if teken.isdigit() in word:
            teller += 1
        
    return teller