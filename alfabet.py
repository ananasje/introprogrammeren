
def compare(word1: str, word2: str) -> int:
    """
    >>> compare("T", "Lana")
    1
    >>> compare("shark", "sWoRd")
    -1
    >>> compare("Daantje", "Daan")
    1
    >>> compare("amanda", "Amanda")
    0
    >>> compare("abc", "abcd")
    -1
    """
    for index in range(min(len(word1), len(word2))):
        letter1 = word1[index].lower()
        letter2 = word2[index].lower()

        if letter1 < letter2:
            return -1

        if letter1 > letter2:
            return 1

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
