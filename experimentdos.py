def replace_positions(s: str, positions: list[int]) -> str:
    nieuwestr = ''

    for i in range(len(s)):
        if i in positions:
            nieuwestr += "#"
        else:
            nieuwestr += s[i]

    # Wat moet je teruggeven?