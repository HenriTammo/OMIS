import töökoda

nimekiri = ["rehvi vahetus", "auto pesu", "värvimine"]
kontroll = True
kokku = 0
while kontroll == True:
    print (nimekiri)
    töö = input("Millist tööd soovid")
    if töö in nimekiri:
        if töö == "rehvi vahetus":
            kokku = kokku + töökoda.rehviVahetus()
        soov = input("Kas soovite veel midagi(y/n)")
        if soov == "y":
            continue
        else:
            break
    else:
        print("Palun valige midagi mis on nimekirjas")

print ("Teie arve on", kokku)