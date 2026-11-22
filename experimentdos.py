def count_length_jumps(words: list[str], minimum: int) -> int:
    teller = 0
    for i in range (1, len(words)):
        if len(words[i]) - lenwords[i - 1] >= minimum:
            teller += 1
            
    return teller