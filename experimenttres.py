def is_long(word: str) -> bool:
    if len(word) > 5:
        return False
    else:
        return True

woord = input("Geef een woord en we tellen de letters:")
print(is_long(woord))
    