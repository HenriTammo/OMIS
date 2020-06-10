from datetime import *

kuupäev = datetime.now().day
fail = open("tund9\õpilased.txt", "r", encoding="UTF-8")
nimed = []
for rida in fail :
    rida.strip()
    nimed.append(rida)

print (nimed[kuupäev-1])




print()