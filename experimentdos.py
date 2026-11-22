def count_length_jumps(words: list[str], minimum: int) -> int:
    """
    Schrijf precies vier doctests.
    """
    teller = 0
    for word in words:
        if len(word) < 