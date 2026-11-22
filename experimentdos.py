def find_length_jumps(
    words: list[str], minimum: int
) -> list[int]:
    """
    Schrijf precies vier doctests.
    """
    nieuwelst = []
    for i in range (1,len(words)):
        if words[i] - words[i - 1]