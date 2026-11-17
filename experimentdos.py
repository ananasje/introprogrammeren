def encrypt(s: str) -> str:
    """
    >>> encrypt("abc")
    'zyx'
    >>> encrypt("hello")
    'svool'
    >>> encrypt("")
    ''
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse = "zyxwvutsrqponmlkjihgfedcba"
    resultaat = ""
    for teken in s:
        for pos in range(len, alphabet):
            if alphabet[pos] == teken:
                resultaat += reverse[pos]