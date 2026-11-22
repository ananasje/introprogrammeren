def partition_by_length(
    words: list[str], minimum: int
) -> list[list[str]]:
    """
    >>> partition_by_length(["boom", "a", "fiets", ""], 4)
    [['boom', 'fiets'], ['a', '']]
    """
    eerstelst = []
    tweedelst = []
    
    for woord in words:
        if len(woord) >= minimum:
            eerstelst.append(woord)
        else:
            tweedelst.append(woord)
        
    return [eerstelst, tweedelst]