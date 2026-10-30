def nth_leap_year(start: int, n: int) -> int:
    """
    >>> nth_leap_year(2000, 1)
    2000
    >>> nth_leap_year(1800, 1)
    1804
    >>> nth_leap_year(2000, 3)
    2008
    >>> nth_leap_year(1896, 3)
    1908
    >>> nth_leap_year(1999, 2)
    2004
    """
    found = 0
    while found < n:
        if is_leap_year(start) == True:
            found = found + 1
        start = start + 1 
    return(start-1)
