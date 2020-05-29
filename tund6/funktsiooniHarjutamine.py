def arvutus(tehe, nimekiri):
    vastus = 0
    check = 0
    if tehe == "liitmine":
        for x in (nimekiri):
            vastus += x
    elif tehe == "lahutamine":
        for x in (nimekiri):
            if vastus == 0 and check == 0:
                vastus = x
                check = 1
            else:
                vastus -= x
    elif tehe == "korrutamine":
        vastus = 1
        for x in (nimekiri):
            vastus *= x
    elif tehe == "jagamine":
        for x in (nimekiri):
            if vastus == 0 and check == 0:
                vastus = x
                check = 1
            else:
                vastus /= x
    else:
        print("Antud tehet ei olnud valikus")
        return None
    return vastus
tehe = input("Millist tehet soovite teha")
mituArvu = int(input("Mitu arvu sisestad"))
nimekiri = []
for x in range(mituArvu):
    arv = float(input("Sisesta arv:"))
    nimekiri.append(arv)
vastus = arvutus(tehe, nimekiri)
print (vastus)