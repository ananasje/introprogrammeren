def is_schrikkel(jaar: int) -> bool:
    """
    >>> is_schrikkel(2024)
    True
    >>> is_schrikkel(2023)
    False
    >>> is_schrikkel(2300)
    False
    """
    if jaar % 400 == 0:
        return True
    elif jaar % 100 == 0:
        return False
    elif jaar % 4 == 0:
        return True
        
    else:
        return False


if __name__ == '__main__':
    jaar = int(input("Geef een jaartal: "))

    if is_schrikkeljaar(jaar):
        print(f"{jaar} is een schrikkeljaar!!")
    else:
        print(f"{jaar} is geen schrikkeljaar.")