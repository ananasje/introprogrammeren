def list_count_element(lst: list[object], elt: object) -> int:
    aantal = 0
    for number in lst: 
        if number == elt:
            aantal += elt
        return aantal


def list_count_even(lst: list[int]) -> int:
    aantal = 0

prin