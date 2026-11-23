def count_digit_groups(s: str) -> int:
    """
    >>> count_digit_groups("abc12def345x6")
    3
    >>> count_digit_groups("12345")
    1
    >>> count_digit_groups("")
    0
    >>> count_digit_groups("a1b2c3")
    3
    """
    group = False
    teller = 0
    for teken in s:
        if teken.isdigit():
            group = True
            
        
        else:
            group = False
    return teller
                
                
            