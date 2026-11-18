def count_long_words(s: str) -> int:
    """
    >>> count_long_words("kat olifant hond")
    2
    >>> count_long_words("  appel   peer ")
    2
    >>> count_long_words("Python")
    1
    >>> count_long_words("")
    0
    >>> count_long_words("a bb ccc")
    0
    """
    teller = 0
    
    for woord in s:
        for teken in woord:
            