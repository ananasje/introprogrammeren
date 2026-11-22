def replace_positions(s: str, positions: list[int]) -> str:
"""
    >>> replace_positions("clown", [1, 3])
    'c#o#n'
    >>> replace_positions("taart", [])
    'taart'
    >>> replace_positions("", [7])
    ''
    >>> replace_positions("draai", [2, 2])
    'd#aai'
    
    """
    nieuwestr = ''

    for i in range(len(s)):
        if i in positions:
            nieuwestr += "#"
        else:
            nieuwestr += s[i]

    return nieuwestr