def longest_streak(lst: list[int]) -> int:
    teller = 0
    for pos in range(1, len(lst)):
        if lst[pos] == lst[pos - 1]:
            teller += 1
        else:
            teller = 1

    if teller > record:
        record = teller
            
    return teller