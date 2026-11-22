def replace_positions(s: str, positions: list[int]) -> str:
    """
    >>> replace_positions(("clown", [1, 3]))
    'c#o#n'
    >>> replace_positions(("taart", [0]))
    '#aart'
    >>> replace_positions(("", [7]))
    ''
    """
    nieuwestr = ''

    for i in range(len(s)):
        if i in positions:
            nieuwestr += "#"
        else:
            nieuwestr += s[i]

    return nieuwestr