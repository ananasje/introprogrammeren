def vowely_words(words: list[str]) -> list[str]:
    resultaat = []

    for woord in words:
        aantal = 0

    for teken in woord:
        if teken.lower() in "aeiou":
            aantal+= 1
        
    if aantal >= 2:
        resultaat.append(woord)

    return resultaat