def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    
    >>> meal("2:00")
    
    >>> meal("7:59")
    'ontbijt'
    
    >>> meal("18:01")
    'avondeten'
    """
    
    uur_str, minuten_str = time.split(":")
    uur = int(uur_str)
    minuten = int(minuten_str)

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
    
    else:
        return None
        

if __name__ == '__main__':
    uur = input("Hoe laat is het?")
    eten = meal(uur)
    if eten is not None:
    
        print("Het is tijd voor", eten)