def reverse_long_words(sentence: str, minimum: int) -> str:
    """
    >>> reverse_long_words("ik eet boterham", 4)
    'ik eet mahretob'
    """
    
    for teken in sentence:
        if teken != " ":
            teller += 1
        
        else:
            