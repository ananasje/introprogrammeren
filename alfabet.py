
def compare(word1: str, word2: str) -> int:
    """
    >>> compare("T", "L")
    1
    >>> compare("shark", "sWoRd")
    -1
    >>> compare("Daantje", "Daan")
    1
    >>> compare("amanda", "Amanda")
    0
    >>> compare("appelblauwzeegroen", "towel")
    -1
    """
    index = 0

    while index < len(word1) and index < len(word2):
        letter1 = word1[index].lower()
        letter2 = word2[index].lower()

        if letter1 < letter2:
            return -1

        if letter1 > letter2:
            return 1

        index += 1

    if len(word1) < len(word2):
        return -1

    if len(word1) > len(word2):
        return 1

    return 0


if __name__ == '__main__':
    word1 = input("Woord 1: ")
    word2 = input("Woord 2: ")

    result = compare(word1, word2)

    if result == -1:
        print(word1 + " first")
    elif result == 1:
        print(word2 + " first")
    else:
        print("No need to decide!")

