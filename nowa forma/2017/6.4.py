with open("Dane_PR2/dane.txt", "r") as o:
    content = [y.split(" ") for y in o.readlines()]
    najdluzszyCiag = 0
    sprawdzanyCiag = 1
    for x in range(320):
        for y in range(199):
            if content[y][x] == content[y+1][x]:
                sprawdzanyCiag += 1
            else:
                if sprawdzanyCiag > najdluzszyCiag:
                    najdluzszyCiag = sprawdzanyCiag
                sprawdzanyCiag = 1
    print(najdluzszyCiag)
