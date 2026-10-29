#the hitchhikers guide to the galaxy
def check_answer(answer: str) -> bool:
    """
    >>> check_answer(42)
    True
    >>> check_answer(tweeenveertig)
    True
    >>> check_answer(tweeënveertig)
    True
    >>> check_answer(zes maal negen)
    False
    
    """
    if answer == 42:
        True
    or answer == "tweeenveertig":
        True
    elif answer == "tweeënveertig":
        True
    else:
        False
if __name__ == '__main__':
  answer= str(input("Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij?"))
  
  if check_answer(answer):
      print("h")
else: 
    print()
    