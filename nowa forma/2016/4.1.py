brzegowe = []
wewnetrzne = 0
a = b = r = 200
with open("Dane_PR2/punkty.txt", "r") as o:
    content = [xy[:-1].split(" ") for xy in o.readlines()]
    for xy in content:
        x, y = xy
        rownanie = pow(int(x) - a, 2) + pow(int(y) - b, 2)
        if rownanie < pow(r, 2):
            wewnetrzne += 1
        elif rownanie == pow(r, 2):
            brzegowe.append(xy)

print(wewnetrzne, brzegowe)
