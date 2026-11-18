def decode_letters(s: str) -> str:
    """
    >>> decode_letters("abc")
    'bcd'
    >>> decode_letters("xyz")
    'yza'
    >>> decode_letters("hello world")
    'ifmmp xpsme'
    >>> decode_letters("")
    ''
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse = "zyxwvutsrqponmlkjihgfedcba"
    
    for pos in range(len(s))