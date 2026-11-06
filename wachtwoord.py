def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.
    >>> 
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
    """
    hoofdletter = False
    kleineletter = False
    for letter in password:
        if letter.isupper(password) and letter.islower(password):
            return True
def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.
    """
    for number in password:
        if number.isdigit(password):
            return True
    
def check_password(password: str) -> bool:
    for password 

if __name__ == '__main__':
    <Hoofdprogramma mag maar één functie aanroepen>