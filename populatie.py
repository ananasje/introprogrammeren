def calculate_years(start_size: int, end_size: int) -> int:
    """
    >>> calculate_years(1200, 1300)
    1
    >>> calculate_years(9, 18)
    8
    >>> calculate_years(20, 100)
    20
    >>> calculate_years(100, 1000000)
    115
    >>> calculate_years(1000, 1083)
    1
    """
    years = 0

    while start_size < end_size:
        born = start_size // 3
        died = start_size // 4

        start_size = start_size + born - died
        years = years + 1

    return years


if __name__ == '__main__':
    start_size = int(input("Startgrootte: "))

    while start_size < 9:
        start_size = int(input("Startgrootte: "))

    end_size = int(input("Eindgrootte: "))

    while end_size <= start_size:
        end_size = int(input("Eindgrootte: "))

    result = calculate_years(start_size, end_size)
    print(f"Jaren: {result}")