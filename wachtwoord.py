def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.
     >>> check_length("appelblauwzeegroen")
    True
    >>> check_length("miauw")
    False
    >>> check_length("muggengeheugen")
    True
    """
    if len(password) == 8 or len(password) > 8:
        return True
    else:
        return False
def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.
    Gebruik een loop om door password te lopen.
     >>> check_letter("Appelblauwzeegroen")
    True
    >>> check_letter("hoi")
    False
    >>> check_letter("abcdefghi")
    True
    """
    hoofdletter = False
    kleineletter = False
    for letter in password:
        if letter.isupper():
            return True
        if letter.islower():
            return True
def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.
    """
    for number in password:
        if number.isdigit():
            return True
    
    return False
def check_password(password: str) -> bool:
    for dingen in password:
        if (check_letter(password) 
            and check_number(password) 
            and check_length(password))  == True:
                return True
        else:
            return False

if __name__ == '__main__':
    wachtwoord = input("Geef een wachtwoord:")
    if (check_password(wachtwoord)) == True:
        print("Het gegeven wachtwoord is valide.")
    else:
        print("Het gegeven wachtwoord is niet valide.")
        
    
    
    
    