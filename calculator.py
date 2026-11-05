def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    """
    x, y, z = evaluate.split(" ")
    x = int(x)
    z = int(z)
    
    if y == "+":
        return x + y
        
    elif y == "-":
        return x - y

if __name__ == '__main__':
    <Invoer, verwerken, functie, uitvoer>