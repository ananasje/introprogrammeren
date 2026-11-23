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
            woord += teken
            
        else:
            if len(woord) >= minimum:
                for letter in woord:
                    if letter
    
                
                