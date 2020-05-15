kujund = input("ruut või ristkülik")

if kujund == "ruut":
    külg = float(input("Sisesta ruudu külg"))
    pindala = külg**2
    ümbermõõt = 4*külg
    print ("Ruutu pindala on", pindala, "cm, ning ümbermõõt on", ümbermõõt, "cm")
elif kujund == "ristkülik":
    külg_1 = float(input("Sisesta esimene külg"))
    külg_2 = float(input("Sisesta teine külg"))
    pindala = külg_1*külg_2
    ümbermõõt = (külg_1+külg_2)*2
    print ("Ruutu pindala on", pindala, "cm, ning ümbermõõt on", ümbermõõt, "cm")
else:
    print ("sisestasite tundmatu sõna")