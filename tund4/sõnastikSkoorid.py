sõnastik = {
    "Erkki" : 2500,
    "Andri" : 1400,
    "Karen" : 1500,
    "Laura" : 2450
    } #siin on mängija nimed ja nende punktid

nimekiri1 = []
nimekiri2 = []
maksimaalne = 0
for x, y in sõnastik.items(): # x-iga võtame nimed ja y-iga skoorid
    counter = 0 #nullime tsükli sees, et see liiga suureks ei läheks
    if y > maksimaalne: #kui skoor on suurem kui eelnev maksimum, siis lisa algusesse
        maksimaalne = y
        nimekiri1.insert(0, x)
        nimekiri2.insert(0, y)
    else: #kui skoor on väiksem kui maksimum
        for z in  range (len(nimekiri1)): #võrdleb teiste skooridega, et leida asukoht
            if len(nimekiri2) < 2: #kui nimekirjas ainult üks inimene, siis lisa kohe lõppu
                nimekiri1.append(x)
                nimekiri2.append(y)
            elif y > nimekiri2[counter]: #kui punkti summa on suurem kui nimekirjas olev summa, siis lisa selle ette ja lõpeta tsükkel
                nimekiri1.insert(counter, x) #positsiooni kätte andmine
                nimekiri2.insert(counter, y)
                break
            counter = counter + 1
print (nimekiri1)
print (nimekiri2)
        