def remove_vowels(s: str) -> str:
    """
    >>> remove_vowels("Amsterdam 2026!")
    'mstrdm 2026!'
    >>> remove_vowels("aieeee ouuuuu")
    ''
    >>> remove_vowels("gn klnkrs hr")
    'gn klnkrs hr'
    >>> remove_vowels("gn klnkrs hr")
    'gn klnkrs hr'
    
    """
    nieuwestr = ""
    klinkers = "AEIOUaeiou"
    for teken in s:
        if teken in klinkers:
            nieuwestr += ""
        else:
            nieuwestr += teken
    
    return nieuwestr