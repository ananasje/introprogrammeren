def is_even_digit(teken: str) -> bool:
    """
    >>> is_even_digit("4")
    True
    >>> is_even_digit("7")
    False
    >>> is_even_digit("a")
    False
    """
    if teken % 2 == 0:
        return True
    else:
        return False


def count_even_digits(s: str) -> int:
    """
    >>> count_even_digits("a2b48")
    3
    >>> count_even_digits("13579")
    0
    >>> count_even_digits("2026")
    4
    """
    Teller = 0
    for teken in s:
        if (is_even_digit(s)) == True:
        Teller += 1
        
        
        