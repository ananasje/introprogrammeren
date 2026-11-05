def filter_a(words: list[str]) -> list[str]:
    filteringvan_a = []
    for word in words:
        if word[0] = "a":
            filteringvan_a.append(word)
    
    return filteringvan_a
    
print filter_a(["appel", "banaan", "aardbei", "kiwi", "ananas"])