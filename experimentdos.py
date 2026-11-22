def partition_by_length(
    words: list[str], minimum: int
) -> list[list[str]]:
    """
    >>> partition_by_length(["boom", "a", "fiets", ""], 4)
    [['boom', 'fiets'], ['a', '']]
    
    >>> partition_by_length(["appel", "moes"], 2)
    [['appel', 'moes'], []]
    
    >>> partition_by_length(["een", "twee"], 5)
    [[], ['een', 'twee']]
    
    >>> partition_by_length([], 7)
    [[], [""]]
    
    """
    eerstelst = []
    tweedelst = []
    
    for woord in words:
        if len(woord) >= minimum:
            eerstelst.append(woord)
        else:
            tweedelst.append(woord)
        
    return [eerstelst, tweedelst]