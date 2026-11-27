def last_digit_position(s: str) -> int:
    """
    >>> last_digit_position("abc123xyz")
    5
    >>> last_digit_position("7dagen")
    0
    >>> last_digit_position("abc")
    -1
    >>> last_digit_position("")
    -1
    """
    
    for teken in s:
        if teken.isdigit()