def meal(time: str) -> str | None:
    
    uur, minuten = time.split(":")
    uur = int(uur)
    minuten = int(minuten)
    
    if uur == 7:
        return "ontbijt"
        
    elif uur == 8 and minuten == 0:
        return "ontbijt"
        
    elif uur == 12:
        return "lunch"
    
    elif uur == 13 and minuten == 0:
        return "lunch"
    
    elif uur == 18:
        return "avondeten"
        
    elif uur == 19 and minuten == 0:
        return "avondeten"
    
    Else:
        return None
        



if __name__ == '__main__':
    if meal is not none:
        
    uur = input("Hoe laat is het?")
    
    print("Het is tijd voor" + meal)