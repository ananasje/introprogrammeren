def shout(text: str) -> str:
    nieuwe_string = ""
    for letter in zin:
        if letter in zin:
            nieuwe_string += letter.isupper()
    return nieuwe_string
if __name__ == '__main__':
    invoer = input("")
    print(shout(invoer))
    
    
    
    