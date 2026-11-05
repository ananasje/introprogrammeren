def count_big(numbers: list[int]) -> int:
    teller = 0
    for getal in numbers:
        if numbers > 10:
        teller = teller + 1
    return teller 
        

numbers = [5, 12, 3, 20, 15]
print(count_big(numbers))