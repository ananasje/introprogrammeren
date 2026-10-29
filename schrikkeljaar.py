def is_schrikkeljaar(jaar: float) -> bool:
    """
    >>> is_schrikkeljaar(2024)
    True
    >>> is_acidic(1200)
    False
    >>> is_acidic(7.0)
    False
    """
    if jaar / 4:
        return True
    elif jaar / 100:
        return False
    elif jaar / 400:
        return True
        
    else:
        return False


if __name__ == '__main__':
    jaar = float(input("Geef een jaartal: "))

    if is_scrhikkeljaar(jaar):
        print("Het is een scrhikkeljaar!!")
    else:
        print("Het is een geen schrikkeljaar.")