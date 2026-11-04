def is_long(word: str) -> bool:
    if len(word) < 5:
        return False
    else:
        return True

woord = input("")
print(is_long(woord))
    