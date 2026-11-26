def select_capitalized(words: list[str]) -> list[str]:
    """
    >>> select_capitalized(["Amsterdam", "fiets", "aB", "AUTO", "Kat"])
    ['Amsterdam', 'AUTO', 'Kat']
    """
    nieuwelst = []
    for woord in words:
        if i in range(len(woord)):
            if woord[0].isupper():
            nieuwelst.append(woord)
    
    return nieuwelst