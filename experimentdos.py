def replace_positions(s: str, positions: list[int]) -> str:
    """
    replace_positions(("kl))
    """
    nieuwestr = ''

    for i in range(len(s)):
        if i in positions:
            nieuwestr += "#"
        else:
            nieuwestr += s[i]

    return nieuwestr