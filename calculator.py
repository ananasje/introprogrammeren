def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    """
    x, y, z = evaluate.split(" ")
    getal = int(x)
    getall = int(z)
    
    if y == "+":
        totaal = getal + getall
        return totaal
        
    elif y == "-":
        totaal = getal - getall
        return totaal
    
    elif y == "*":
        totaal = getal * getall
        return totaal
    
    elif y == "/":
        totaal = getal / getall
        return totaal
        

if __name__ == '__main__':
    invoer = input(" ")
    print(evaluate("invoer"))


