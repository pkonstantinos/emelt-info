bekert = input("Max 255 karakter szöveg")

jo = True
def bekeres(adat):
    if len(adat) > 255 or len(adat) == 0:
        print("A beírt meghaladta a 255 karaktert")
        global bekert
        bekert = input("Max 255 karakter szöveg")
    else:
        global jo
        jo = False


while jo:
    bekeres(bekert)


ekezetek : dict = {
    "ö" : "o",
    "ü" : "u",
    "ó" : "o",
    "ő" : "o",
    "ú" : "u",
    "é" : "e",
    "á" : "a",
    "ű" : "u",
    "í" : "i"
}

def atalakito(adat):

    for key, value in ekezetek.items():
        adat = adat.lower()
        adat = adat.replace(key, value)

    abc_stringkent = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    abc = [abc for abc in abc_stringkent]

    new_bekert = ""

    for betu in adat:
        if abc.__contains__(betu.upper()):
            new_bekert += betu.upper()
    return new_bekert

bekert = atalakito(bekert)

kulcsszo = input("Kulcsszo ")
jo = True
def bekeres(adat):
    if len(adat) > 5 or len(adat) == 0:
        print("A beírt meghaladta az 5 karaktert")
        global kulcsszo
        kulcsszo = input("Kulcsszo ")
    else:
        global jo
        jo = False


while jo:
    bekeres(kulcsszo)




kulcsszo = atalakito(kulcsszo)



osszefuzott = []

for i in range(len(bekert)):
    for k in range(len(kulcsszo)):
        osszefuzott.append(kulcsszo[k])

for i in range(abs(len(bekert) - (len(bekert)* len(kulcsszo)))):
    osszefuzott.pop(-1)

osszefuzott_string = ""
for i in osszefuzott:
    osszefuzott_string += i


f = open("Vtabla.dat", "r", encoding="UTF-8")

files = f.readlines()

adatok = [file.strip() for file in files]

kodolt = ""

x, y = [], []

for i in bekert:
    for k in range(len(adatok[0])):
        if i == adatok[0][k]:
            y.append(k)

for m in osszefuzott_string:
    for l in range(len(adatok[0])):
        if m == adatok[0][l]:
            x.append(l)

for i in range(len(x)):
    kodolt += adatok[y[i]][x[i]]


wr = open("kodolt.dat", "w")

wr.write(kodolt)
wr.close()

print(kodolt)
















