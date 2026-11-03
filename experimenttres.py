geld = 0
weken = 0
storting=int(input("hoeveel krijg je per week?"))

while geld < 100:
    geld = geld + storting
    weken = weken +1

print(weken)