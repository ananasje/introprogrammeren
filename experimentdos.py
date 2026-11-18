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
    nieuwestring = ""
    for teken in s:
        if teken == " ":
            nieuwestring += " "
        for teken in range(len(alphabet)):
            if teken == alphabet(i):
                nieuwestring +=  25 - alphabet(i)
            