with open("Dane_PR2/dane.txt", "r") as o:
    odrzucic = 0
    linie = [x.split(" ") for x in o.readlines()]
    for linia in linie:
        linia = [int(x) for x in linia]
        for i in range(320 // 2 - 1):
            if linia[i] != linia[320 - i - 1]:
                odrzucic += 1
                break

    print(odrzucic)
