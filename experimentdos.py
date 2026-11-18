def count_long_words(s: str) -> int:
    """
    >>> count_long_words("kat olifant hond")
    2
    >>> count_long_words("  appel   peer ")
    2
    >>> count_long_words("Python")
    1
    >>> count_long_words("")
    0
    >>> count_long_words("a bb ccc")
    0
    """
    huidige_lengte = 0
aantal = 0

    for teken in s:
    if teken == " ":
        # Het woord is afgelopen
    else:
        huidige_lengte += 1