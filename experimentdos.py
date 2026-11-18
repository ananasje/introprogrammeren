def count_digit_groups(s: str) -> int:
    """
    >>> count_digit_groups("ab12cd345x6")
    3
    >>> count_digit_groups("12345")
    1
    >>> count_digit_groups("abc")
    0
    >>> count_digit_groups("1a2b3")
    3
    >>> count_digit_groups("")
    0
    """
    newlist = []
    groep = false
    cijfer = 0
    
    for teken in s:
        if teken.isdigit():
            
            
            
            