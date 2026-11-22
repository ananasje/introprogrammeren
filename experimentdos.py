def count_vowels(s: str) -> int:
    """
    >>> count_vowels("Amsterdam")
    3
    >>> count_vowels("GN KLNKRS")
    
    """
    teller = 0
    klinkers = "aAiIOoUuEe"
    for i in len(s) :
        if s[i] in klinkers:
            teller += 1
    return teller