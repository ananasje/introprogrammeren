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
    else:
        return False


if __name__ == '__main__':
    ph = float(input("Geef een pH-waarde: "))

    if is_acidic(ph):
        print("Het is een zuur")
    else:
        print("Het is een base")