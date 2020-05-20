muutuja = 20
nimekiri = []
for x in range(muutuja): #x muutub iga tsükliga suuremaks
    nimekiri.append(x)
print (nimekiri)

for number in nimekiri:
    print(nimekiri[number])
    
for y in range(10):
    if y > 6:
        break
    else:
        print (y)