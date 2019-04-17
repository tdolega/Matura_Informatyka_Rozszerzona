k = 107
wyniki = []
with open("Dane_PR2/dane_6_1.txt", "r") as o:
    content = o.readlines()
    for word in content:
        word = word[:-1]
        zaszyfrowane = ""
        for char in word:
            a = ord(char) - 65
            a += k
            a %= 26
            a += 65
            a = chr(a)
            zaszyfrowane += a
        wyniki.append(zaszyfrowane + "\n")

with open("wyniki_6_1.txt", "w") as o:
    o.writelines(wyniki)
