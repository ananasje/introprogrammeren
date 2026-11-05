def has_book(books: list[str], title: str) -> bool:
    bibliotheek = ["Dune", "1984", "Frankenstein"]
    for title in bibliotheek:
        if title:
            return True
        
    
boekje = "Dracula"
print(has_book(["Dune", "1984", "Frankenstein"], "Dracula"))