def camelcase(text: str) -> str:
    """
    >>> 
    """
    nieuwe_string = ""
    for letter in text:
        if letter.isupper() == True:
            nieuwe_string += "_" 
        
        else:
            nieuwe_string += letter
    
    return nieuwe_string

if __name__ == '__main__':
    case = input("")
    print(camelcase(case))
    
    