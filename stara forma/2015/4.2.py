w = 0
with open("Dane_PR2/slowa.txt", "r") as o:
    for slowo in o.readlines():
        bloki = [slowo[0]]
        for char in slowo[1:-1]:
            if char != bloki[-1]:
                bloki.append(char)
        if bloki == ["0", "1"]:
            w += 1
print(w)
