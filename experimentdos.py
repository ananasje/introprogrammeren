def encrypt(s: str) -> str:
    """
    >>> encrypt("abc")
    'zyx'
    >>> encrypt("hello")
    'svool'
    >>> encrypt("a b")
    'z y'
    >>> encrypt("")
    ''
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse = "zyxwvutsrqponmlkjihgfedcba"
    nieuwe_string = ""
    for teken in s:
        if teken in alphabet:
            teken[pos]
            