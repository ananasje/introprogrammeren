def check_input(dna: str) -> bool:
    """
    >>> check_input('miauw')
    False
    >>> check_input('AGCT')
    True
    """
    for elements in dna:
        if elements not in "AaGgCcTt":
            return False
        
        return True
def transcribe_dna_to_rna(dna: str) -> str:
    """
    >>> transcribe_dna_to_rna('miauw')
    'That is not a valid DNA string'
    >>> transcribe_dna_to_rna('AgCt')
    'That is not a valid DNA string'
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
        print("RNA:" , transcribe_dna_to_rna(invoer))
    else:
        print("That is not a valid DNA string")
    
    