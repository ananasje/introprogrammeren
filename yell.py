def yell(text: str) -> str:
    """
    >>>
    x
    """
    nieuwe_string = ""
    for teken in text:
        if teken == "!":
            nieuwe_string += "!"
        elif teken == ".":
            nieuwe_string += "!!"
        elif teken == "?":
            nieuwe_string += "!!"

if __name__ == '__main__':
    zinnetje = input("")
    print(yell(zinnetje))