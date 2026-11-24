def first_zero(values: list[int]) -> int:
    
    i = 0

    while i < len(values):
        if values[i] == 0:
            return i

        i += 1

    return -1   
        
            