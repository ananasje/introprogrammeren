for teken in s:
    if teken.lower() in "aeiou":
        klinkers += 1
    elif teken.isalpha():
        medeklinkers += 1
    elif teken == " ":
        woorden += 1
        
letters = klinkers + medeklinkers
leesniveau =(medeklinkers-tklinkers)**2 * letters/woorden
return (medeklinkers-tklinkers)**2 * letters/woorden