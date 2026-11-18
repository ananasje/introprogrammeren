def longest_valid_word(words: list[str]) -> str:
    """
    >>> longest_valid_word(["kat", "auto", "olifant", "boom"])
    'olifant'
    >>> longest_valid_word(["boom", "maan", "fiets"])
    'fiets'
    >>> longest_valid_word(["kat", "bus", "xyz"])
    ''
    >>> longest_valid_word([])
    ''
    """
    teller == 0
    tellerklinkers == 0
    for woord in words:
        klinker == 0
        for letter in woord:
            if letter 