def compute_score(word: str) -> int:
    """
    >>> compute_score("code")
    7
    >>> compute_score("CAT")
    5
    >>> compute_score("!!!")
    0
    """
    POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
             1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    teller = 0
    for pos in range(len(alphabet)):
        if alphabet[pos] == letter.lower():
            teller += POINTS[pos]
        return 
    return 0