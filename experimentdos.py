def partition_by_length(
    words: list[str], minimum: int
) -> list[list[str]]:
    """
    >>> partition_by_length(appel, moes)
    """
    eerstelst = []
    tweedelst = []
    
    for woord in words:
        if len(woord) >= minimum:
            eerstelst.append(woord)
        else:
            tweedelst.append(woord)
        
    return [eerstelst, tweedelst]