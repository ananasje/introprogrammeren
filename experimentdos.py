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
    nieuwestring = ""
    for pos in range (len(s)):
        if s[pos] in alphabet:
            alphabet[pos] == reverse[pos]
            nieuwestring += reverse
            
            