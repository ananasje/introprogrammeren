def partition_by_length(
    words: list[str], minimum: int
) -> list[list[str]]:
    """
    Schrijf hier precies vier doctests,
    waaronder een test met een lege lijst.
    """
    eerstelst = []
    tweedelst = []
    
    for woord in words:
        if len(woord) >= minimum:
            eerstelst.append(woord)
        else:
            tweedelst.append(woord)
        
    return eerstelst, tweedelst