def interleave(lt1: list[object],lt2: list[object],keep: bool) -> list[object]:
    resultaat = []

    kortste = min(len(lt1), len(lt2))

for pos in range(kortste):
    resultaat.append(ltt1[pos])
    resultaat.append(lijst2[pos])
