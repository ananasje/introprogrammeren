def count_a(word: str) -> int:
    teller=0
    for letter in word:
        if letter == "a":
            teller = teller + 1
            
    return teller 

print(count_a("bann"))