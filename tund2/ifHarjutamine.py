tingimus = True #teine variant on False
if tingimus == True: 
    print ("Vastab tõele")
    tingimus = False
    
if tingimus == True:
    print ("midagi on valesti")
else:
    print ("kõik on korras")
    
arv = 10

if arv < 5: #< on väiksem ja > on suurem
    print (arv, "on väiksem kui viis")
elif arv >= 10: #elif ei pea lisama enam else lõppu/kasutades >= vaatame suurem võrdne
    print ("arv vastab soovile")
    
sõna = "Henri Tammo"
if sõna != "Henri Tammo":
    print ("Tere", sõna)
else:
    print ("sõna ei olnud see mis arvasin")
    
arv1 = 6
arv2 = 20
if arv1 > 2 and arv2 < 100: #and võib esineda nii mitu korda kui vaja
    print ("arvud sobivad")

if arv1 == 100 or arv2 == 20: #or samuti võib kasutada nii mitu korda kui vaja
    if arv2 < 30:
        print ("See ei ole väga suur arv")
    print ("vähemalt üks arv sobib")
    
