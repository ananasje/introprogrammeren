def total_cheap(prices: list[int]) -> int:
    zeer_goedkoop = []
    totaal = 0
    for getal in prices:
        if getal < 20:
            totaal = totaal + getal
        
    return zeer_goedkoop
print(total_cheap([10, 25, 5, 30, 15]))