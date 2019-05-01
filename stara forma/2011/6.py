with open("Dane_PR/liczby.txt", "r") as o:
    liczby = o.readlines()
    parzyste = ilec = sumac = 0
    for liczba in liczby:
        if liczba[-2] == "0":
            parzyste += 1
        if len(liczba) - 1 == 9:
            ilec += 1
            sumac += int(liczba, 2)
    print("a) parzyste:", parzyste)
    max = max([int(x, 2) for x in liczby])
    print("b) max dwojkowo", bin(max)[2:], "i max dziesietnie:", max)
    print("c) jest", ilec, "takich liczb a ich suma wynosi", bin(sumac)[2:])
