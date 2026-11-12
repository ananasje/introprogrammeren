def longest_word_from_list(lst: list[str]) -> str:
    lang_wrd = ""
    
    for woord in lst:
        if len(woord) > len(lang_wrd):
        lang_wrd = woord
            
    return lang_wrd
    
def print_banner(lst: list[str]) -> None:
    langste = longest_word_from_list(lst)
    hekjes = "#" * len(langste)

    print(hekjes)

    for word in lst:
        print(word)
    
    print(hekjes)
    
    
def string_to_list(text: str) -> list[str]:
    """
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

    nieuwe_lijst = []
    
    
    