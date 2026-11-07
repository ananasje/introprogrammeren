def camelcase(text: str) -> str:
    """
    >>> camelcase('camelCase')
    'camel_case'
    >>> camelcase('waterMeloen')
    'water_meloen'
    """
    nieuwe_string = ""
    for letter in text:
        if letter.isupper() == True:
            nieuwe_string += "_" 
            nieuwe_string += letter.lower()
        else:
            nieuwe_string += letter
    
    return nieuwe_string

if __name__ == '__main__':
    case = input("camelCase:")
    print("snake_case:", camelcase(case))
    
    