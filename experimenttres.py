def sum_even_numbers(n: int) -> int:
    totaal = 0
    
    for getal in range(0, n + 1):
        if getal % 2 == 0:
            totaal = totaal + getal 
    return totaal
        
    
if __name__ == '__main__':
    getal = int(input("Welk getalletje?"))
    print(sum_even_numbers(getal))