ph=float(input("Geef een PH-waarde:"))
def is_acidic(ph:float) -> bool:
if ph < 7.0:
    return(true)
else:
    return(false)
    print("Het is een base")