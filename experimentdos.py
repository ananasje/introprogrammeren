for teken in s:
    if teken.lower() in "aeiou":
        klinkers += 1
    elif teken.isalpha():
        medeklinkers += 1
    elif teken == " ":
        woorden += 1
        
letters = klinkers + medeklinkers
return