import random
elu = 3
while elu > 0:
    arv1 = random.randint(0, 10)
    arv2 = random.randint(0, 10)
    print ("Mis on", arv1, "*", arv2)
    vastus = int(input("Vastus:"))
    if vastus == (arv1 * arv2):
        print ("Väga tubli")
    else:
        print ("Pead veel õppima")
        elu -= 1
print ("Mäng läbi")