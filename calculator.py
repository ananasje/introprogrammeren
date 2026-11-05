def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    
    >>> 
    """

    if y == "+":
        totaal = x + z
        return float(totaal)

    elif y == "-":
        totaal = x - z
        return float(totaal)

    elif y == "*":
        totaal = x * z
        return float(totaal)

    elif y == "/":
        totaal = x / z
        return float(totaal)


if __name__ == '__main__':
    invoer = input()
    x_tekst, y, z_tekst = invoer.split()

    x = int(x_tekst)
    z = int(z_tekst)

    print(evaluate(x, y, z))
        




