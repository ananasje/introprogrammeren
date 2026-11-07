def yell(text: str) -> str:
    """
    >>> yell("i did, what u gonna do about it?")
    "i did, what u gonna do about it?"
    
    >>> yell("cooked.")
    "cooked."
    
    """
    nieuwe_string = ""
    for teken in text:
        if teken == "!":
            nieuwe_string += "!!"
        elif teken == ".":
            nieuwe_string += "."
        elif teken == "?":
            nieuwe_string += "??"
        else:
            nieuwe_string += teken
            
    return nieuwe_string

if __name__ == '__main__':
    zinnetje = input("")
    print(yell(zinnetje))