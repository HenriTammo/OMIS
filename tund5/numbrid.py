import random

file = open("numbrid.txt", "w")

for x in range(1000):
    file.write(str(random.randint(1, 100)) + "\n")
file.close()

file = open("numbrid.txt", "r")
nimekiri = []
for x in(file):
    x = x.strip()
    nimekiri.append(int(x))

maksimum = 0
hulk = 0

for x in range(len(nimekiri)):
    if maksimum < nimekiri[x]:
        maksimum = nimekiri[x]
        hulk = 0
    if maksimum == nimekiri[x]:
        hulk = hulk + 1
print(maksimum, hulk)