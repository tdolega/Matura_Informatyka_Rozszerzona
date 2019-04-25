w = 0
with open("Dane_PR2/slowa.txt", "r") as o:
    for slowo in o.readlines():
        l0 = l1 = 0
        for char in slowo[:-1]:
            if char == "0":
                l0 += 1
            else:
                l1 += 1
        if l0 > l1:
            w += 1
print(w)
