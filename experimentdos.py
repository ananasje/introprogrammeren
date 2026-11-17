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
     
    for teken in s:
        for pos in range(len, alphabet):
            if alphabet[pos] == teken:
                re