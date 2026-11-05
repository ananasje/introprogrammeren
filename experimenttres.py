def highest_grade(grades: list[int]) -> int:
    hoogste = grades[0]
    for getal in grades:
        if getal > hoogste:
return getal
        
cijfers = ([4, 7, 9, 3, 8, 6])

print(highest_grade(cijfers))