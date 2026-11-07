def camelcase(text: str) -> str:
    """
    >>> 
    """
    nieuwe_string = ""
    for letter in text:
        if letter in text.isupper():
            nieuwe_string+= "_"

if __name__ == '__main__':
    case = input("")
    print(camelcase(case))
    
    