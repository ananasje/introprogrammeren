def longest_digit_block(s: str) -> int:
    """
    >>> longest_digit_block("abc123de45")
    3
    >>> longest_digit_block("a12b3456c")
    4
    >>> longest_digit_block("abc")
    0
    >>> longest_digit_block("12345")
    5
    >>> longest_digit_block("")
    0
    """
    aantal = 0
    langste = 0
    for teken in s:
        if teken.isdigit():
            aantal += 1
            
        if teken.isalpha():
            
        if aantal < langste:
            langste = aantal
            aantal = 0
    return langste
            
        
        
        
        