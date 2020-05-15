thisList = ["Tere", 5, 7.9, 4, 6, 8]
print (thisList)

print (thisList[0]) #võtab esimese
print (thisList[-1]) #võtab viimase

print (thisList[2:5]) #vahemiku määramine

positsioon = 1
print (thisList[positsioon]) #muutuja kasutamine et positsiooni saada

arv = thisList[-1] #muutuja omistus nimekirjaga

thisList[2] = 100
print (thisList)
print (len(thisList)) #kontrollime nimekirja pikkust

thisList.append("lisamine lõppu")
thisList.insert(1, "täpne lisamine")
print (thisList)

thisList.remove(6) #vaatab väärtust
thisList.pop(0) #kui pop() on tühi, siis võtab viimase elemendi
print (thisList)