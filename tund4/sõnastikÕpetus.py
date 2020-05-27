sõnastik = {
    "audi" : 2007,
    "bmw" : "suunatuli katki",
    "ford" : 1967
    }

print (sõnastik)
sõnastik["audi"] = 1980
print (sõnastik["audi"])

for x in sõnastik.values(): #kasutades .values() saame objektide väärtused
    print (x)
    
for x, y in sõnastik.items():
    print (x, y) #x on objekt ja y on selle väärtus
    
print(len(sõnastik))

del sõnastik["bmw"] #objekti ja ta väärtuse eemaldamine
print (sõnastik)

sõnastik["mazda"] = "roostetab palju"
print (sõnastik)