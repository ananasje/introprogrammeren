def count_long_words(words: list[str]) -> int:
    """
    >>> count_long_words(["kat", "school", "fiets"])
    2
    >>> count_long_words(["boom", "aap", "zon"])
    0
    >>> count_long_words(["STRAND", "auto", "boom"])
    1
    >>> count_long_words([])
    0
    """
    klinker = "aeiou"
    count = 0
    
    for woord in words:
        
        for teken in woord:
            if teken.lower() not in klinker:
                klinker >= 2
                count += 1
                
    return count