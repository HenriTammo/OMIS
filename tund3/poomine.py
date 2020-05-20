elu = 9
sisestus = input("Sisesta sõna")
sisestusList = list(sisestus)
pikkus = len(sisestusList)
valmis = []
for x in range(pikkus):
    valmis.append("_")
while elu > 0:
    print (valmis)
    if valmis == sisestusList:
        print("tubli, arvasid ära")
        break
    täht = input("Paku tähte")
    counter = 0
    arvamus = 0
    for x in list(sisestus):        
        if täht == x:
            valmis[counter] = täht
            arvamus += 1
        counter += 1
    if arvamus == 0:
        print("tähte polnud")
        elu -= 1
print("test")