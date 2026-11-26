def select_capitalized(words: list[str]) -> list[str]:
    """
    >>> select_capitalized(["Amsterdam", "fiets", "aB", "AUTO", "Kat"])
    ['Amsterdam', 'AUTO', 'Kat']
    >>> select_capitalized(["vIS", "baLl", "kLoK", "auto", "tReiInN"])
    []
    >>> select_capitalized([])
    []
    >>> select_capitalized(["Amsterdam", "fiets", "aB", "AUTO", "Kat"])
    ['Amsterdam', 'AUTO', 'Kat']
    """
    nieuwelst = []
    
    for woord in words:
        if woord[0].isupper():
            nieuwelst.append(woord)
    
    return nieuwelst