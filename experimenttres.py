def sum_big(numbers: list[int]) -> int:
    
    for getal in numbers:
        if getal > 10:
            getal = getal + getal
    return getal
    
print(sum_big([5, 12, 3,, 15]))