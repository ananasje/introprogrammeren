def remaining_battery(kilometers: int) -> int:
    return 100 - (kilometers * 3)
    
    
if __name__ == '__main__':
    
    
    kilometers= int(input("Hoeveel kilometers wil je afleggen?"))
    print(remaining_battery(kilometers))