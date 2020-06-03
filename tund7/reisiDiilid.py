file = open("tund7/asukohad.txt", "r")

counter = 1
nimekiri = []
for asukoht in file:
    asukoht = asukoht.strip()
    nimekiri.append(asukoht)
    print(str(counter) + "." + asukoht)
    counter += 1

valik = int(input("Kuhu reisida soovid, vali number"))
print (nimekiri[valik-1])