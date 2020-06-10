toonid = ["valge", "must", "punane", "sinine","eridisain"]
viimistlus = ["matt", "läikiv","kristall"]
pesuPaketid =["ise", "standard", "eskort"]
def rehviVahetus():
    rattaMõõt = int(input("Mitme tollised rehvid on?"))
    if rattaMõõt <= 16:
        rehviHind = 150
    elif rattaMõõt > 16 and rattaMõõt < 20:
        rehviHind = 200
    else:
        rehviHind = 250
    return rehviHind
def autoPesu():
    teenus = input("Millist teenust soovite?")
    if teenus == "ise":
        pesuHind = 10
    if teenus == "standard":
        pesuHind = 40
    if teenus =="eskort":
        pesuHind = 120
    return pesuHind

def värvimine():
    toon = input("Millist värvitooni soovite?")
    print(viimistlus)
    värv = input("Kuidas värvime?")
    
    if toon == "valge" or  "must " or "sinine" or "punane" and värv == "matt":
        värviHind = 50
    if toon == "valge" or  "must " or "sinine" or "punane" and värv == "läikiv":
        värviHind = 75
    if toon == "valge" or  "must " or "sinine" or "punane" and värv == "kristall":
        värviHind = 100
    if toon == "eridisain":
        värviHind = 250
    return värviHind
        