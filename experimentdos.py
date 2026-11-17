def compute_letter_score(letter: str) -> int:
    """
    >>> compute_letter_score("a")
    1
    >>> compute_letter_score("C")
    3
    >>> compute_letter_score("z")
    10
    """
    POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
             1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    resultaat = ""
    for teken in s:
        for pos in range(len(alphabet)):
            if alphabet[pos] == teken:
                resultaat += pos()
                


