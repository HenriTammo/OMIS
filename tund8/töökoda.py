def rehviVahetus():
    rattaMõõt = int(input("Mitme tollised rehvid on?"))
    if rattaMõõt <= 16:
        rattaHind = 150
    elif rattaMõõt > 16 and rattaMõõt < 20:
        rattaHind = 200
    else:
        rattaHind = 250
    return rattaHind
