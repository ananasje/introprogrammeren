def print_collatz(n: int) -> None:
    """
    >>> print_collatz(3)
    7
    22
    11
    34
    
    >>> print_collatz(1)
    1
    """
    print(n)

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

        print(n)

def collatz_length(n: int) -> int:
    """
    Berekent de lengte van de Collatz-reeks.

    >>> collatz_length(3)
    8
    >>> collatz_length(1)
    1
    >>> collatz_length(6)
    9
    """
    count = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

        count = count + 1

    return count