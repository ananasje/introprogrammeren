def has_book(books: list[str], title: str) -> bool:
    for boek in books:
        if boek == title:
            return True

    return False


bibliotheek = ["Dune", "1984", "Frankenstein"]
boekje = "Dracula"

print(has_book(bibliotheek, boekje))