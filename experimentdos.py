def count_length_jumps(words: list[str], minimum: int) -> int:
    teller = 0
    for i in len(words):
        if words[i] - words[i - 1] >= minimum:
            teller += 1
            
    return teller