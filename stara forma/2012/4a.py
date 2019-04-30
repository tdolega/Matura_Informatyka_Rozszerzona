szyfrowane = [x.replace("\n", "") for x in open("Dane_PR/tj.txt", "r").readlines()]
klucze = [x.replace("\n", "") for x in open("Dane_PR/klucze1.txt", "r").readlines()]
wynik = open("wynik4a.txt", "w")
for i in range(len(szyfrowane)):
    szyfrowana = szyfrowane[i]
    klucz = klucze[i]
    szyfr = ""
    for j in range(len(szyfrowana)):
        ls = ord(szyfrowana[j])
        lk = ord(klucz[j % len(klucz)]) - 64
        lz = ls + lk
        if lz > 90:
            lz -= 26
        szyfr += chr(lz)
    wynik.write(szyfr + "\n")
wynik.close()
