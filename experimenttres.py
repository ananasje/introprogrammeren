def is_long(word: str) -> bool:
    if len(word) > 5:
        return True
    else:
        return False

woord = input("Geef een woord en we tellen de letters:")
print(is_long(woord))
    