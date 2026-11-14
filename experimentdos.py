def count_vowels(word: str) -> int:
    """
    >>> count_vowels("olifant")
    3
    >>> count_vowels("Python")
    1
    >>> count_vowels("AEIOU")
    5
    >>> count_vowels("")
    0
    """
    aantal = 0
    for teken in str:
        if teken.upper() == "AEIOU":
            aantal += 1 
        else:
            aantal == aantal
            
        return aantal 
            