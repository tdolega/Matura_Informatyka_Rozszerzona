with open("Dane_PR2/dane.txt", "r") as o:
    linie = [x.split(" ") for x in o.readlines()]
    gmax = 0
    for x in range(320):
        lmax = 1
        for y in range(200 - 1):
            if linie[y][x] == linie[y+1][x]:
                lmax += 1
            else:
                if lmax > gmax:
                    gmax = lmax
                lmax = 1
    print(gmax)
