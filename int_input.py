def get_positive_int() -> int:
    """
    Vraagt om een positief geheel getal (1 of hoger).
    """
    result = int(input("Enter a positive int: "))

    while result < 1:
        result = int(input("Enter a positive int: "))

    return result


def get_any_int_but_0() -> int:
    """
    Vraagt om een geheel getal dat niet 0 is.
    """
    result = int(input("Enter an int but not 0: "))

    while result == 0:
        result = int(input("Enter an int but not 0: "))

    return result


def get_min_int(minimum: int) -> int:
    """
    Vraagt om een geheel getal dat minstens minimum is.
    """
    result = int(input("Enter an int: "))

    while result < minimum:
        result = int(input("Enter an int: "))

    return result


def get_two_different_ints() -> tuple[int, int]:
    """
    Vraagt om twee verschillende gehele getallen.
    """
    number1 = int(input("Enter first int: "))
    number2 = int(input("Enter second int: "))

    while number1 == number2:
        number1 = int(input("Enter first int: "))
        number2 = int(input("Enter second int: "))

    return number1, number2


if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()