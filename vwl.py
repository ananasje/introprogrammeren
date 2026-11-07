def vowelremover(zin: str) -> str:
    """
    >>> vowelremover('hoedje van papier')
    'hdj vn ppr'
    vowelremover('ik vouw papier, kom niet zeggen dat je mr vouwt')
    'hdj vn ppr'
    """
    nieuwe_string = ""
    for woord in zin:
        if woord in "aAeEiIoOuU":
            nieuwe_string += ""
        else:
            nieuwe_string += woord
    return nieuwe_string
        
if __name__ == '__main__':
    zin = input("")
    print(vowelremover(zin))