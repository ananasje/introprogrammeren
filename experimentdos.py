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
    medeklinkers = 0
    
    for woord in words:
        
        for teken in woord:
            if teken.isalpha() and teken.lower() not in "aeiou":
                medeklinkers += 1
                teken >= 2
                count = 0
                
    return count