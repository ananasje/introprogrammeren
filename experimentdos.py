def longest_word_length(s: str) -> int:
    huidige_lengte = 0
    langste_lengte = 0

    for teken in s:
        if teken == " "