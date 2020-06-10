sisestus = True
õppeained = []
klassiruumid = []
while sisestus == True:
    aine = input("Sisesta õppeaine nimetus")
    õppeained.append(aine)
    klass = input("Sisesta õppeklass")
    klassiruumid.append(klass)
    rohkem = input("Soovid veel midagi sisestada? (y/n)")
    if rohkem == "y":
        continue
    else:
        sisestus = False

ainekava = {}
for x in range (len(õppeained)):
    ainekava[õppeained[x-1]] = klassiruumid[x-1]
print(ainekava)