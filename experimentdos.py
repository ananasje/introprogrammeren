def select_not_lower(strs: list[str]) -> list[str]:
    """
    Schrijf hier je 4 doctests.
    """
    # Jouw oplossing
    new_lis = []
    for word in strs:
        if word not in strs:
            new_lis.append(word)
    
    return new_lis
             
            
    
    