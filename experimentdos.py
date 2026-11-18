def has_digit(word: str) -> bool:
    """
    >>> has_digit("abc3")
    True
    >>> has_digit("hello")
    False
    >>> has_digit("")
    False
    """
    if word.isdigit():
        return True
        
    return False

def count_strong_words(words: list[str]) -> int:
    """
    >>> count_strong_words(["abc12", "hi3", "hello", "Python7"])
    2
    >>> count_strong_words(["12345", "abcde", "a1"])
    1
    >>> count_strong_words([])
    0
    """
    teller = 0
    for word in words:
        if has_digit(word)
        