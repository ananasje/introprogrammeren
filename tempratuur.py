def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet Celsius om naar Fahrenheit of andersom.

    >>> convert_temperature("C", 37)
    98
    >>> convert_temperature("F", 104)
    40
    >>> convert_temperature("C", -40)
    -40
    >>> convert_temperature("F", 212)
    100
    >>> convert_temperature("c", 15)
    59
    >>> convert_temperature("f", 50)
    10
    """
    if old_type.upper() == "C":
        return int((18 * old_temp + 320) / 10)
    else:
        return int((10 * old_temp - 320) / 18)


def print_table(old_type: str, begin_temp: int,
                end_temp: int, step_size: int) -> None:
    """
    Print een conversietabel met temperaturen.

    >>> print_table("C", -10, 0, 5)
      C |   F
    -10 |  14
     -5 |  23
      0 |  32
    >>> print_table("F", 32, 38, 3)
      F |   C
     32 |   0
     35 |   1
     38 |   3
    >>> print_table("C", 10, 0, 2)
      C |   F
    """
    old_type = old_type.upper()

    if old_type == "C":
        new_type = "F"
    else:
        new_type = "C"

    print(f"{old_type:>3} | {new_type:>3}")

    for temp in range(begin_temp, end_temp + 1, step_size):
        converted = convert_temperature(old_type, temp)
        print(f"{temp:>3} | {converted:>3}")


if __name__ == '__main__':
    old_type = input("Welke eenheid van temperatuur (C of F)? ")

    while old_type.upper() != "C" and old_type.upper() != "F":
        old_type = input("Welke eenheid van temperatuur (C of F)? ")

    begin_temp = int(input("Wat is de begintemperatuur? "))
    end_temp = int(input("Wat is de eindtemperatuur? "))

    step_size = int(input("Wat is de stapgrootte? "))

    while step_size <= 0:
        step_size = int(input("Wat is de stapgrootte? "))

    print_table(old_type, begin_temp, end_temp, step_size)