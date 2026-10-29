def is_schrikkeljaar(jaar: int) -> bool:
    """
    >>> is_schrikkeljaar(2024)
    True
    >>> is_schrikkeljaar(1200)
    False
    >>> is_schrikkeljaar(1100)
    False
    """
    if jaar % 400 == 0:
        return True
    elif jaar % 100== 0:
        return False
    elif jaar 
        return True
        
    else:
        return False


if __name__ == '__main__':
    jaar = float(input("Geef een jaartal: "))

    if is_schrikkeljaar(jaar):
        print("Het is een schrikkeljaar!!")
    else:
        print("Het is een geen schrikkeljaar.")