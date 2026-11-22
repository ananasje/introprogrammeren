def select_shorter_words(
    words: list[str], minimum: int
) -> list[str]:
    """
    Schrijf precies vier doctests.
    """
    nieuwelst = []
    for i in range(1, len(words)):
        if words[i] <= minimum:
            nieuwelst.append