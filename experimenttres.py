def has_book(books: list[str], title: str) -> bool:
    bibliotheek = ["Dune", "1984", "Frankenstein"]
    for title in bibliotheek:
        if title:
            return True
        else:
            return False
    
boekje = "Dracula"
print(has_book([bibliotheek, "Dracula"))