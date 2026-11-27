def last_digit_position(s: str) -> int:
    """
    >>> last_digit_position("abc123")
    3
    >>> last_digit_position("7dagen")
    0
    >>> last_digit_position("geen cijfers")
    -1
    >>> last_digit_position("")
    -1
    """
    
    for i in range (len(s)):
        if s[i].isdigit():
            return i
    
    