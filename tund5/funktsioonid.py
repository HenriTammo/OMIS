import välisFunktsioon
def esimene(sisse):
    print(sisse)
def teine():
    x = 3
    y = 5
    print (x + y)
def kolmas():
    x = 5
    y = 10
    return x*y #niimodi saab funktsioonist väärtuse kätte
def neljas(esimene, teine, kolmas):
    kokku = esimene + teine + kolmas
    return kokku
sõna = "Tere funktsioon"
esimene(sõna)

teine()
number = kolmas()
print (number)
x = 10
y = 20
z = 30
vastus = neljas(x, y, z)

välisFunktsioon.välimine()