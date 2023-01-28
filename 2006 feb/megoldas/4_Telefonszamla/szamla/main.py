import math


csucsidok = [7*60*60, 18*60*60]

mobil_tarsasag = {
    "belul" : 67.175,
    "kivul" : 46.675
}

vezetekes_tarsasag = {
    "belul" : 30,
    "kivul" : 15
}

class Hivas:
    def __init__(self, mettol, meddig, telefonszam, vezetekes, csucsido):
        self.mettol : list = mettol
        self.meddig : list= meddig
        self.telefonszam = telefonszam
        self.vezetekes : bool = vezetekes
        self.csucsido = csucsido


def masodpercben(lista):
    return int(lista[0])*60*60 + int(lista[1])*60 + int(lista[2])
hivasok = []


f = open("HIVASOK.TXT", "r", encoding="UTF-8")

files = f.readlines()

for i in range(1, len(files), 2):
    hivas = files[i - 1].strip().split()
    hivas_kezdet = [hivas[0], hivas[1], "0"]
    hivas_vege = [int(hivas[3]), int(hivas[4]), int(hivas[5])]

    if hivas_vege[2] > 0:
        hivas_vege[2] = 0
        hivas_vege[1] += 1
        if hivas_vege[1] == 60:
            hivas_vege[1] = 0
            hivas_vege[0] += 1



     #hivas
    telefonszam = files[i].strip() #telefonszam
    vezetekes = False
    csucsido = False

    if(telefonszam[0] + telefonszam[1] == "39" or telefonszam[0] + telefonszam[1] == "71" or telefonszam[0] + telefonszam[1] == "41"):
        vezetekes = False
    else:
        vezetekes = True
    if csucsidok[0] < masodpercben([int(hivas[0]), int(hivas[1]), int(hivas[2])]) < csucsidok[1]:
        csucsido = True
    else:
        csucsido = False

    new_hivas = Hivas(hivas_kezdet,
                      hivas_vege,
                      telefonszam,
                      vezetekes,
                      csucsido
                      )
    hivasok.append(new_hivas)



#####

bekeres = input("Telefonszám: ")

for hivas in hivasok:
    if hivas.telefonszam == bekeres:
        print("Megtaláltam a telefonszámot")
        break
else:
    print("A megadott telefonszám nincs a listán")


hivas_kezdete = input("Kezdet: ")
hivas_vege = input("Vége: ")

hivas_kezdete = hivas_kezdete.split(" ")
hivas_vege = hivas_vege.split(" ")

print(f"A hívás pontosan: {(masodpercben(hivas_vege) - masodpercben(hivas_kezdete)) / 60} percig tartott")


for hivas in hivasok:
    print(f"{(masodpercben(hivas.meddig) - masodpercben(hivas.mettol))/60} {hivas.telefonszam}")


csucsidon_belul = 0
csucsidon_kivul = 0

for i in hivasok:
    if i.csucsido:
        csucsidon_belul += 1
    else:
        csucsidon_kivul +=1

print(f"Csúcsidőn belül: {csucsidon_belul} \n Csúcsidőn kívül: {csucsidon_kivul}")


vezetekessel = 0
mobilossal = 0
for hivas in hivasok:
    if hivas.vezetekes:
        vezetekessel += (masodpercben(hivas.meddig) - masodpercben(hivas.mettol)) / 60
    else:
        mobilossal += (masodpercben(hivas.meddig) - masodpercben(hivas.mettol))/60

print(f"V: {vezetekessel} \n M: {mobilossal}")

osszesites = 0
for hivas in hivasok:
    if hivas.csucsido:
        if hivas.vezetekes:
            osszesites += (((masodpercben(hivas.meddig) - masodpercben(hivas.mettol))/60)) * vezetekes_tarsasag["belul"]
        else:
            osszesites += ((masodpercben(hivas.meddig) - masodpercben(hivas.mettol)) / 60) * mobil_tarsasag["belul"]

print(f"Összesen ennyit fizetett csúcsidőért: {int(osszesites)} Ft")



