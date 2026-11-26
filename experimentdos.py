def remove_vowels(s: str) -> str:
    """
    >>> remove_vowels("Amsterdam 2026!")
    'mstrdm 2026!'
    >>> remove_vowels("Br 2026!")
    'mstrdm 2026!'
    """
    nieuwestr = ""
    klinkers = "AEIOUaeiou"
    for teken in s:
        if teken in klinkers:
            nieuwestr += ""
        else:
            nieuwestr += teken
    
    return nieuwestr