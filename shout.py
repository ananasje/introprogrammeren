def shout(text: str) -> str:
    """
    >>> shout('MIAUW')
    'MIAUW'
    >>> shout('stan stayc')
    'STAN STAYC'
    >>> shout('stREam stAyC')
    'STREAM STAYC'
    """
    nieuwe_string = ""
    for letter in text:
        if letter in text:
            nieuwe_string += letter.upper()
    return nieuwe_string


if __name__ == '__main__':
    zin = input("")
    print(shout(zin))
    
    
    
    