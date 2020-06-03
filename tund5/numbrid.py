from turtle import *
 
def ruut():             # Defineerime funktsiooni nimega ruut
    i = 0
    while i < 4:
        forward(100)
        left(90)
        i = i + 1                 # Kutsume funktsiooni ruut välja. Kilpkonn joonistab ruudu küljega 100 pikslit
    right(10)# Pöörame paremale 45°
    ruut()                  # Kutsume uuesti funktsiooni ruut välja
ruut()
exitonclick()