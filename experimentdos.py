def count_special_words(words: list[str]) -> int:
    """
    >>> count_special_words(["Abc1", "hello", "X9"])
    2
    >>> count_special_words(["ABC", "123", "a1"])
    0
    >>> count_special_words(["A12B", "Z7", "test5"])
    2
    >>> count_special_words([])
    0
    """
    teller = 0

    for word in words:
        cijfer = 0
        hoofd = 0

        for teken in word:# Als teken een
             cijfer is: verhoog cijfer
            # Als teken een hoofdletter is: verhoog hoofd

        if cijfer >= 1 and hoofd >= 1:
            teller += 1

    return teller