def sum_big(numbers: list[int]) -> int:
    totaal = 0
    for getal in numbers:
        if getal > 10:
            totaal = totaal + getal
    return getal
    
print(sum_big([5, 12, 3, 20, 15]))