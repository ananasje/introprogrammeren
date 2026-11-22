def select_shorter_words(
    words: list[str], minimum: int
) -> list[str]:
    """
    >>> select_shorter_words(["computer", "kat", "olifant", "ik"], 3)
    ['kat', 'ik']
    >>> select_shorter_words([], 1)
    []
    >>> select_shorter_words(["zeveraar", "sjarel", "dommerik"], 4)
    []
    >>> select_shorter_words(["je", "sjarel", "dommerik"], 4)
    []
    """
    nieuwelst = []
    for i in range(1, len(words)):
        if len(words[i]) <= minimum:
            nieuwelst.append(words[i])
            
        return nieuwelst