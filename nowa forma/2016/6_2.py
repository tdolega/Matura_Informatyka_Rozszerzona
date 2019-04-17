wyniki = []
with open("Dane_PR2/dane_6_2.txt", "r") as o:
    content = o.readlines()
    i = 0
    for word in content:
        word, k = word.split(" ")
        k = k[:-1]
        zaszyfrowane = ""
        for char in word:
            a = ord(char) - 65
            a -= int(k)
            a %= 26
            a += 65
            a = chr(a)
            zaszyfrowane += a
        wyniki.append(zaszyfrowane + "\n")
        i+=1
        # generalnie zadanie jest zepsute dlatego nie analizuję całego pliku
        if i > 715:
            break

with open("wyniki_6_2.txt", "w") as o:
    o.writelines(wyniki)
