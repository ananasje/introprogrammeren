def has_book(books: list[str], title: str) -> bool:
    bibliotheek = ["Dune", "1984", "Frankenstein"]
    for boek in bibliotheek:
        if boek:
            return True
        
    
boekje = "Dracula"
print(has_book(boekje))