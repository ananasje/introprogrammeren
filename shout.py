def shout(text: str) -> str:
    """
    >>> shout('MIAUW')
    'MIAUW'
    
    """
    nieuwe_string = ""
    for letter in zin:
        if letter in zin:
            nieuwe_string += letter.upper()
    return nieuwe_string


if __name__ == '__main__':
    zin = input("")
    print(shout(zin))
    
    
    
    