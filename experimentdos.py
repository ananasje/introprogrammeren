def special_sort(l: list[int]) -> list[int]:

    i = 0
    j = i + 1
    
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
    l[i], l[j] = l[j], l[i]
        
        