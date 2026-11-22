def count_big_drops(values: list[int]) -> int:
    """
    >>>count_big_drops([10, 6, 5, 1, 9])
    2
    >>>count_big_drops([1, 3, 5])
    0
    """
    teller = 0
    for i in range (1,len(values)):
            if values[i] < values[i - 1] 
            teller += 1
    
    return teller