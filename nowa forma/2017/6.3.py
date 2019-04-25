def sprawdz_somsiaduf(tab, x2, y2):
    pixel = int(tab[y2][x2])
    if x != 0:
        if abs(pixel - int(tab[y2][x2-1])) > 128:
            return 1
    if x != 319:
        if abs(pixel - int(tab[y2][x2+1])) > 128:
            return 1
    if y != 0:
        if abs(pixel - int(tab[y2-1][x2])) > 128:
            return 1
    if y != 199:
        if abs(pixel - int(tab[y2+1][x2])) > 128:
            return 1
    return 0


with open("Dane_PR2/dane.txt", "r") as o:
    content = [y.split(" ") for y in o.readlines()]
    kontrastujace = 0
    for y in range(200):
        for x in range(320):
            kontrastujace += sprawdz_somsiaduf(content, x, y)
    print(kontrastujace)
