def replace_positions(s: str, positions: list[int]) -> str:
    """
    >>> replace_positions(("clown", [1, 3]))
    'c#o#n'
    >>> replace_positions(("clown", [1, 3]))
    'c#o#n'
    """
    nieuwestr = ''

    for i in range(len(s)):
        if i in positions:
            nieuwestr += "#"
        else:
            nieuwestr += s[i]

    return nieuwestr