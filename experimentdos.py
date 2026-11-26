def select_lowercase_words(words: list[str]) -> list[str]:
    """
    >>> select_lowercase_words(["appel", "Boom", "fiets", "AUTO"])
    ['appel', 'fiets']
    >>> select_lowercase_words([])
    []
    >>> select_lowercase_words([])
    []
    """
    nieuwelst = []
    for word in words:
        if word.islower():
            nieuwelst.append(word)
        
    return nieuwelst