from math import *
from xml.etree.ElementTree import PI # kõik funktsionid moodulist
# imprt math     potom nada pisat :math.funktsioon()

print("Tere tulemast") #vivodit informaciju na ekran
nimi=input("mis sinu nimi on?") #sisend lugemise jaoks input()->str
print() # tühi rida
print(f"{nimi}, sul on väga ilus nimi!") #print(nimi,", sul on väga ilus nimi!")
vanus=int(input("kui vana sa oled?")) # int(str)
print(nimi,"","sa oled",vanus,"aastat vana")
vanus+=10
print(nimi+", 10 aastat pärast sa oled "+str(vanus)+"aastat vana")

print()
print("võrdse pindalaga ristkükik ja ring")
a=float(input("skala laius: "))
b=float(input("skala pikkus: "))
S=a*b #-, +, ** ,/, // , %
P=2*a+2*b
d=round(sqrt(a**2+b**2)) #ümardamine 2 numbrist koma pärast
d=sqrt(a**2+b**2)
print(f"pindala ={S}\nDiagonaal = {d}")
print("ringi raadius")
c=float(pi*r**2)
r=float(sqrt(S/pi))





