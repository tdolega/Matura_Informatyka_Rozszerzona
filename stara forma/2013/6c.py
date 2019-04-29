wynik = []
with open("Dane_PR/dane.txt", "r") as o:
    for line in o.readlines():
        pcyfra = 0
        zaliczac = True
        for cyfra in line.replace("\n", ""):
            if int(cyfra) < pcyfra:
                zaliczac = False
            pcyfra = int(cyfra)
        if zaliczac:
            wynik.append(int(line))
print(len(wynik), "spełniają warunek, z największą liczbą", max(wynik), "oraz najmniejszą", min(wynik))
