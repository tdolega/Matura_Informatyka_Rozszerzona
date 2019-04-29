wynik = 0
with open("Dane_PR/dane.txt", "r") as o:
    for line in o.readlines():
        line = line.replace("\n", "")
        if line[0] == line[-1]:
            wynik += 1
print(wynik)
