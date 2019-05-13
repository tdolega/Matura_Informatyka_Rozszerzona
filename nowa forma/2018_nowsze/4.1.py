with open("Dane_PR2/sygnaly.txt", "r") as o:
    o = o.readlines()
    for i in range(39, 1000, 40):
        print(o[i][9], end="")
