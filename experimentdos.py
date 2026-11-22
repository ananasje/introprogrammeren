def find_length_jumps(
    words: list[str], minimum: int
) -> list[int]:
    """
    >>> find_length_jumps(["ik", "appel", "ja", "computer"], 3)
    [1, 3]
    >>> find_length_jumps(["ik"], 1)
    []
    >>> find_length_jumps([""], 2)
    []
    
    
    """
    nieuwelst = []
    for i in range (1,len(words)):
        if words[i] - words[i - 1] >= minimum:
            nieuwelst.append(i)
    
    return nieuwelst