def contig(lst: list[int]) -> list[num(int)]:
    nieuwe_lijst:[]
    lege_lijst: []
    for number in range(len(lst)):
        lege_lijst.append(number)
        if number - lst[pos + 1] == -1:
            lege_lijst.append(lst[pos + 1])
            nieuwe_lijst.append(lege_lijst)
            lege_lijst = []
            
    return nieuwe_lijst
if __name__ == '__main__':
    invoer = print(input(int()))