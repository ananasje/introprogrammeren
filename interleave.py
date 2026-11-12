def interleave(lt1: list[object],lt2: list[object],keep: bool) -> list[object]:
    resultaat = []

    kortste = min(len(lt1), len(lt2))

    for pos in range(kortste):
        resultaat.append(lt1[pos])
        resultaat.append(lt2[pos])
    
    if keep == True:
        for pos in range(kortste, len(lt1)):
            resultaat.append(lijst1[pos])

        for pos in range(kortste, len(lt2)):
            resultaat.append(lijst2[pos])