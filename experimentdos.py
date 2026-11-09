def list_count_element(lst: list[object], elt: object) -> int:
    aantal = 0
    for number in lst: 
        if number == elt:
            aantal += elt
        return aantal

lijsta = [1,2,3,3,5]
print(list_count_element(lijsta, 2))

