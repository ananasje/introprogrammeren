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
    >>> check_answer(gewoon een beetje aardig zijn voor elkaar?)
    False
    
    """
    if answer == 42 or answer == "tweeenveertig" or answer == "tweeënveertig":
        True
    else:
        False
if __name__ == '__main__':
  answer = str(input("Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij?"))
  
  if check_answer(answer):
      print("zei Deep Thought, met oneindige majesteit en kalmte.")
      print("PS: ja")
 else: 
     print("zei Deep Thought NIET, met oneindige majesteit en kalmte.")
           print("PS: nee")
    