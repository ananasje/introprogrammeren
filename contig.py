def contig(lst: list[int]) -> list[list[int]]:
    nieuwe_lijst = []
    lege_lijst = []

    for pos in range(len(lst) - 1):
        lege_lijst.append(lst[pos])

        if lst[pos + 1] != lst[pos] + 1:
            nieuwe_lijst.append(lege_lijst)
            lege_lijst = []

    # Hier ontbreekt nog het laatste element
    # En het laatste groepje moet nog opgeslagen worden

    return nieuwe_lijst
