import random
nimekiri = ["Üks", "Kaks", "Kolm"]
for x in nimekiri: #tagastab nimekirjas oleva väärtuse
    print(x)

for y in range (10): #vahemik peab olema sulgudes ja loeb arv väärtust
    print (y)

nimekiri.append("Neli") #append käsklus lisab nimekirja lõppu
nimekiri.insert(0, "Null") #paneb ette antud asukohale uue väärtuse aga ei eemalda eelmist
nimekiri.remove("Üks") #eemaldab nimekirjast etteantud väärtuse
nimekiri.pop(1) #eemaldab asukohal oleva väärtuse, kui sulud tühjaks jätta siis eemaldab viimas elemendi
print (nimekiri)

sõnastik = {
    "python" : "tore keel",
    "java" : "raske keel",
    "php" : "see mulle ei meeldi"
}

del sõnastik["php"] #kustutab etteantud objekti ja selle väärtuse
sõnastik["java"] = "enam ei ole nii raske" #kui ette antud objekt eksisteerib, siis muutab väärtuse
sõnastik["html"] = "hea keel algajale" #kui objekti nimi on selline mida juba ei eksisteeri sõnastikus, siis ta lisab selle koos antud väärtusega
print(sõnastik)


file = open("tund10\spikker.txt", "w")
for x in range(20):
    file.write(str(random.randint(1, 20)) + "\n")
file.close()

file = open("tund10\spikker.txt", "r")
test = file.readline(3)
print(test)
for x in file:
    x = x.strip()
    print(x)
file.close()

def funktsioon(näide):
    näide = näide + näide
    return näide

sõna = "Tere"
pikemSõna = funktsioon(sõna)
print(pikemSõna)