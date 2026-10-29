def is_schrikkeljaar(jaar: float) -> bool:
    """
    >>> is_schrikkeljaar(2.5)
    True
    >>> is_acidic(7.9)
    False
    >>> is_acidic(7.0)
    False
    """
    if jaar / 4:
        return True
    elif jaar / 100:
        return True
    elif jaar / 
    else:
        return False


if __name__ == '__main__':
    jaar = float(input("Geef een jaartal: "))

    if is_scrhikkeljaar(jaar):
        print("Het is een scrhikkeljaar!!")
    else:
        print("Het is een gewoon jaar")