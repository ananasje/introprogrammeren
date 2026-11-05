def small_numbers(numbers: list[int]) -> list[int]:
    small_numbers = []
    for getal in numbers:
        if getal < 10:
            small_numbers.append(getal)
            
    return small_numbers
    
print(small_numbers([4, 15, 7, 20, 3]))