def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.
    
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    
    >>> calculate_grade("Congratulations! Today is your day. You're "
    ...     "off to Great Places! You're off and away!")
    
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    
    """
    letters = 0
    for teken in text:
        if teken.isalpha():
            letter += 1
            
    return teken
    
    woord = 1
    for pos in range(1, len(text)):
        if text[pos - 1] == " " and text [pos].isalpha():
            woord += 1
    
    return woord
    
    zin = 1
    for pos in range(1, len(text)):
        if text[pos - 1] == " ":
            zin += 1
        if text[pos - 1] == " ":
            zin += 1

def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    """

if __name__ == '__main__':
    <Hoofdprogramma>