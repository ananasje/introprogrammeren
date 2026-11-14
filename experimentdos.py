def count_uppercase_words(words: list[str]) -> int:
    """
    >>> count_uppercase_words(["PyTHon", "HELLO", "Python"])
    2
    >>> count_uppercase_words(["ABC", "abc", "aBc"])
    1
    >>> count_uppercase_words([])
    0
    """
    count = 0
    
    for woord in words:
        for teken in woord:
            if teken.isalpha and teken.isupper():
                