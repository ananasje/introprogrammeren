def select_words_with_digits(words: list[str]) -> list[str]:
    """
    >>> select_words_with_digits(["kat", "h0nd", "123", "fiets"])
    ['h0nd', '123']
    >>> select_words_with_digits(["chat", "blap", "blip"])
    []
    >>> select_words_with_digits([""])
    []
    >>> select_words_with_digits(["67", "s6s7", "hunterxhunter"])
    ['67', 's6s7']
    """
    nieuwelst = 
    teller = 0
    for woord in words:
        for teken in woord:
            if teken.isdigit():
                teller += 1
        
        if teller >= 1:
            nieuwelst.append(woord)
            teller = 0
    
    return nieuwelst
                
                
            