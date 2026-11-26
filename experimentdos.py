def select_words_with_uppercase(words: list[str]) -> list[str]:
    """
    >>> select_words_with_uppercase(["appel", "Boom", "fiets", "AUTO", "aB"])
    ['Boom', 'AUTO', 'aB']
    >>> select_words_with_uppercase(["Appel", "BOOm", "fleS", "QUEloQue", "" ])
    ['Appel', 'BOOm', 'QUEloQue']
    """
    nieuwelst = []
    for woord in words:
        hoofdlettergevonden = False
        
        for i in range(len(woord)):
            if woord[i].isupper():
                hoofdlettergevonden = True
                
        if hoofdlettergevonden == True:
            nieuwelst.append(woord)
            
    return nieuwelst