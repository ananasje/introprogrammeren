def first_word(s: str) -> str:
    """
    >>> first_word("ik eet taart")
    'ik'
    >>> first_word("   appel en peer")
    'appel'
    """
    nieuwestring = ""
    for teken in s:
        if teken != ""