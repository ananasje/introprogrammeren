def count_vowels(s: str) -> int:
    """
    Schrijf precies vier doctests.
    """
    teller = 1
    klinkers = "aAiIOoUuEe"
    for word in s:
        if word in klinkers