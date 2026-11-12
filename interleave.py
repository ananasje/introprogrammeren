def interleave(lt1: list[object],lt2: list[object],keep: bool) -> list[object]:
    """
    >>> interleave([6, 7], [6, 8], True)
[6, 6, 7, 8]
>>> interleave([1, 2, 3], [4, 5], False)
[1, 4, 2, 5]
>>> interleave([1, 2, 3], [4, 5], True)
[1, 4, 2, 5, 3]
    """
    resultaat = []

    kortste = min(len(lt1), len(lt2))

    for pos in range(kortste):
        resultaat.append(lt1[pos])
        resultaat.append(lt2[pos])
    
    if keep == True:
        for pos in range(kortste, len(lt1)):
            resultaat.append(lt1[pos])

        for pos in range(kortste, len(lt2)):
            resultaat.append(lt2[pos])
        
    return resultaat