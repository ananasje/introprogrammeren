def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    
    >>> evaluate(2, "+", 2)
    4.0
    >>> evaluate(5, "/", 2)
    2.5
    >>> evaluate(9, "*", 10)
    90.0
        
    """

    if y == "+":
        totaal = float(x + z)
        return totaal

    elif y == "-":
        totaal = float(x - z)
        return totaal

    elif y == "*":
        totaal = float(x * z)
        return totaal

    else:
        totaal = x / z
        return totaal


if __name__ == '__main__':
    invoer = input()
    x_tekst, y, z_tekst = invoer.split()

    x = int(x_tekst)
    z = int(z_tekst)

    print(evaluate(x, y, z))
        




