def selection_sort(l: list[int]) -> list[int]:
    for i in range(len(l) - 1):
        kleinste_pos = i

        for j in range(i, len(l)):
            if l[i] < l[j]:
                kleinste_pos = j

        l[i], l[kleinste_pos] = l[kleinste_pos], l[i]

    return l
        
        