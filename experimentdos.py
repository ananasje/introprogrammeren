def select_words_with_digits(words: list[str]) -> list[str]:
    """
    Schrijf precies vier doctests.
    """
    nieuwelst = ""
    for woord in words:
        for teken in words:
            if teken.isdigit():
                teller += 1
        
        if teller > 1:
            nieuwelst.append(woord)
            teller : 0
    
    return nieuwelst
                
                
            