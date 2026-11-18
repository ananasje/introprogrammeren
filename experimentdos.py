def longest_word_length(s: str) -> int:
    """
    >>> longest_word_length("kat olifant hond")
    7
    >>> longest_word_length("  appel   peer ")
    5
    >>> longest_word_length("Python")
    6
    >>> longest_word_length("")
    0
    """
    teller = 0
    langste = 0
    for teken in s:
        if teken != " ":
            teller += 1
            
        if teken == " ":
            if teller > langste:
                langste =
        