def select_lowercase_words(words: list[str]) -> list[str]:
    """
    >>> select_lowercase_words(["appel", "Boom", "fiets", "AUTO"])
    ['appel', 'fiets']
    """
    
    for word in words:
        if word.islower