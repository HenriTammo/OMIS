nimekiri1 = ["Jaanika", "Erena", "Märt", "Sandra"]
nimekiri2 = [45, 49, 31, 22]

sõnastik = {
    }
counter = 0
for x in nimekiri1:
    sõnastik[x] = nimekiri2[counter]
    counter = counter + 1
print (sõnastik)

for x in sõnastik.values():
    print(x)
    
for x, y in sõnastik.items():
    print(x, y)