def count_vowels(s: str) -> int:
    """
    Schrijf precies vier doctests.
    """
    teller = 1
    klinkers = "aAiIOoUuEe"
    for i in range(len(s)) :
        if s[i] in klinkers:
            teller += 1
    return teller