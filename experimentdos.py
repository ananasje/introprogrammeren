def count_vowels(s: str) -> int:
    """
    >>> count_vowels("Amsterdam")
3
    """
    teller = 1
    klinkers = "aAiIOoUuEe"
    for i in range(len(s)) :
        if s[i] in klinkers:
            teller += 1
    return teller