mc = {}
with open("Dane_PR2/slowa.txt", "r") as o:
    for slowo in o.readlines():
        slowo = slowo[:-1]
        mlc = c0 = 0
        for char in slowo:
            if char == "0":
                c0 += 1
            else:
                c0 = 0
            if c0 > mlc:
                mlc = c0
        if mc.__contains__(mlc):
            mc[mlc].append(slowo)
        else:
            mc[mlc] = [slowo]
print("maksymalna dlugosc:", max(mc), "\nw liczbach", mc[max(mc)])