def last_word(s: str) -> str:
    
    """
    >>> last_word("ik eet taart")
    'taart'
    >>> last_word("  hallo wereld   ")
    'wereld'
    >>> last_word("Python")
    'Python'
    >>> last_word("   ")
    ''
    ''
    """
   huidigewoord = ""
   laatstewoord = ""
   
   for teken in s:
       if teken != " ":
           huidigewoord += teken
    