def longest_word_length(s: str) -> int:
    huidige_lengte = 0
    langste_lengte = 0

    for teken in s:
        if teken == " ":
            if huidige_lengte  > langste_lengte
                huidige_lengte  = langste_lengte
                huidige_lengte = 0
        else:
            huidige_lengte += 1
        
    if huidige_lengte > langste_lengte:
        huidige_lengte  += langste_lengte
    
    return langste_lengte
      