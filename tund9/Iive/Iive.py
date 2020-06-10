fail1 = open("tund9\Iive\synnid.txt", encoding="UTF-8")
fail2 = open("tund9\Iive\surmad.txt", encoding="UTF-8")
sünnid = []
surmad = []

for b in fail1:
    b = b.strip()
    sünnid.append(b)
for d in fail2:
    d = d.strip()
    surmad.append(d)
print(surmad)

counter = 1
for iive in range (len(sünnid)):
    kokku = int(sünnid[iive]) - int(surmad[iive])
    print(str(counter) + "." + str(kokku))
    counter += 1

fail1.close()
fail2.close()

