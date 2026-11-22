def count_vowels(s: str) -> int:
    """
    >>> count_vowels("Amsterdam")
    3
    >>> count_vowels("GN KLNKRS")
    0
    >>> count_vowels("")
    0
    >>> count_vowels("HeEey")
    3
    """
    teller = 0
    klinkers = "aAiIOoUuEe"
    for letter in s :
        if letter in klinkers:
            teller += 1
    return teller