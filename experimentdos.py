def reverse_long_words(sentence: str, minimum: int) -> str:
    """
    >>> reverse_long_words("ik eet boterham", 4)
    'ik eet mahretob'
    """
    nieuwestr = ""
    woord = ""
    omgekeerd = ""
    for teken in sentence:
        if teken != " ":
            teller += 1
            
        else:
            if len(woord) >= minimum:
                
                