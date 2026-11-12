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
    
    
    
    
    nieuwe_lijst = []
    
    
    