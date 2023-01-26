f = open("lottosz.dat", "r")

files = f.readlines()


adatok = [file.strip().split(" ") for file in files]

bekert_adat = "89 24 34 11 64"
#bekert_adat = input("Melyek az 52.hét lottószámai? ")
adatok.append(bekert_adat.split(" "))
adatok[51].sort()
print(adatok[51])

bekert_szam = int(input("Mondj egy számot 1-től 51-ig "))

print(adatok[bekert_szam -1])

szamok = []
hatodik = []
for i in adatok:
    for k in i:
        if not szamok.__contains__(int(k)):
            szamok.append(int(k))
        hatodik.append(int(k))


szamok.sort()
print(len(szamok))
if (len(szamok) < 90):
    print("Van olyan szám")
else:
    print("Nincs olyan szám")

counter = 0

for i in hatodik:
    if i%2 == 0:
        counter+=1
print(f"{counter} szám páros")


w = open("lotto52.ki", "w")

szoveg = r""

for i in files:
    szoveg += i

szoveg += '\n' + bekert_adat
w.write(szoveg)
print(szoveg)

mennyi_van : dict = {

}

for i in range(len(szamok)):
    mennyi_van[szamok[i]] = 0


for key,values in mennyi_van.items():
    for i in range(len(hatodik)):
        if hatodik[i] == key:
            mennyi_van[key] += 1


for key, values in mennyi_van.items():
    print(f"Szám: {key}, db: {values}")

