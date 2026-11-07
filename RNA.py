def check_input(dna: str) -> bool:
    """
    Controleert of de input een correcte DNA-string is.
    Accepteert zowel hoofd- als kleine letters.
    """
    for elements in dna:
        if elements in "AaGgCcTt":
            return True
        else: 
            return False
def transcribe_dna_to_rna(dna: str) -> str:
    """
    Schrijft een string met DNA-elementen in hoofd- en/of kleine
    letters om naar een string met RNA-elementen (als hoofdletters).
    Ga ervan uit dat een valide string wordt gegeven (dus geen
    check aanroepen).
    """
    nieuwe_string2 = ""
    for teken in dna:
        if teken in "Aa":
            nieuwe_string2 += "U"
        elif teken in "Gg":
            nieuwe_string2 += "C"
        elif teken in "Cc":
            nieuwe_string2 += "G"
        else:
            nieuwe_string2 += "A"
        
    return nieuwe_string2
if __name__ == '__main__':
    
    invoer = input("DNA:")
        if (check_input(invoer)) == True:
            print("RNA:"transcribe_dna_to_rna(invoer))
        else:
            print("That is not a valid DNA string")
    
    