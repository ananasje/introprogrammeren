def select_words_with_uppercase(words: list[str]) -> list[str]:
    """
    >>> select_words_with_uppercase(
...     ["appel", "Boom", "fiets", "AUTO", "aB"]
... )
['Boom', 'AUTO', 'aB']
    """
    nieuwelst = []
    for woord in words:
        for i in range(len(woord)):
            if woord[i].isupper():
                