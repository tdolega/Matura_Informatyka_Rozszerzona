zaszyfrowane = [x.replace("\n", "") for x in open("Dane_PR/sz.txt", "r").readlines()]
klucze = [x.replace("\n", "") for x in open("Dane_PR/klucze2.txt", "r").readlines()]
wynik = open("wynik4b.txt", "w")
for i in range(len(zaszyfrowane)):
    zaszyfrowana = zaszyfrowane[i]
    klucz = klucze[i]
    odszyfrowane = ""
    for j in range(len(zaszyfrowana)):
        ls = ord(zaszyfrowana[j])
        lk = ord(klucz[j % len(klucz)]) - 64
        lz = ls - lk
        if lz < 65:
            lz += 26
        odszyfrowane += chr(lz)
    wynik.write(odszyfrowane + "\n")
wynik.close()
