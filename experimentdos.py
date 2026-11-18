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
            nieuwestring += reverse[pos]
            
    return nieuwestring
    
    def encrypt(s: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse = "zyxwvutsrqponmlkjihgfedcba"
    nieuwestring = ""

    for teken in s:
        if teken == " ":
            nieuwestring += " "
        else:
            for pos in range(len(alphabet)):
                if teken == alphabet[pos]:
                    nieuwestring += reverse[pos]

    return nieuwestring