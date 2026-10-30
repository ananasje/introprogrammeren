def print_pyramid(hoogte: int) -> None:
    """
    Print een halve piramide van de gegeven hoogte.

    >>> print_pyramid(3)
      ##
     ###
    ####
    >>> print_pyramid(6)
      ##
     ###
    ####
    ######
    
    >>> print_pyramid(1)
    ##
    """
    for rij in range(1, hoogte + 1):
        spaties = hoogte - rij
        hekjes = rij + 1

        for i in range(spaties):
            print(' ', end='')

        for i in range(hekjes):
            print('#', end='')

        print()


if __name__ == '__main__':
    hoogte = int(input("Hoe hoog moet de piramide zijn? "))

    while hoogte < 1 or hoogte > 23:
        hoogte = int(input("Hoe hoog moet de piramide zijn? "))

    print_pyramid(hoogte)