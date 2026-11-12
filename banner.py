def longest_word_from_list(lst: list[str]) -> str:
    """
    >>> longest_word_from_list(["kat", "cake", "sushi"])
    'sushi'
    """
    lang_wrd = ""

    for woord in lst:
        if len(woord) > len(lang_wrd):
            lang_wrd = woord

    return lang_wrd


def print_banner(lst: list[str]) -> None:
    """
>>> print_banner(["Stan", "Stayc"])
    ######
    Stan
    Stayc
    ######
    """
    langste = longest_word_from_list(lst)
    hekjes = "#" * len(langste)

    print(hekjes)

    for woord in lst:
        print(woord)

    print(hekjes)


def string_to_list(text: str) -> list[str]:
    """
    ['Margherita', 'Tutta', 'la', 'Vita']
    >>> string_to_list("")
    []
    """
    nieuwe_lijst = []
    woord = ""

    for teken in text:
        if teken == " ":
            nieuwe_lijst.append(woord)
            woord = ""
        else:
            woord += teken

    if woord != "":
        nieuwe_lijst.append(woord)

    return nieuwe_lijst


if __name__ == '__main__':
    boodschap = input("Boodschap: ")
    woorden = string_to_list(boodschap)
    print_banner(woorden)

    
    