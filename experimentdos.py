def count_big_drops(values: list[int]) -> int:
    """
    >>>count_big_drops([10, 6, 5, 1, 9])
    2
    """
    teller = 0
    for i in range (3,len(values)):
        if values[i] < values[i - 1] and (values[i] < values[i - 2] 
        and values[i] < values[i - 3]):
            teller += 1
    
    return teller