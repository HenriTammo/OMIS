tõene = True
kokku = 0
while tõene == True:
    kokku = kokku + 1
    if kokku == 10:
        tõene = False #ei lase tsüklil edasi minna
    print (kokku)
print ("Tsükkel lõppes")

kokku = 0
while kokku < 11:
    kokku = kokku + 1
print ("number suurem kui kümme")

kokku = 0
arv = 0
while kokku < 10:
    kokku = kokku + 1
    while kokku < 5: #sisemine tsükkel jookseb nii kaua kui saab
        print ("arv on väiksem kui viis")
        arv = kokku
        ruut = arv**2
        print (ruut, "on see arv ruudus")
        kokku = kokku + 1