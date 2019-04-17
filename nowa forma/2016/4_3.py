import math

wewnetrzne = zewnetrzne = krawedziowe = i = 0
a = b = r = 200
brzegowe = []
checkpoints = []
przyblizenie = []
with open("Dane_PR2/punkty.txt", "r") as o:
    content = [xy[:-1].split(" ") for xy in o.readlines()]
    for xy in content:
        x, y = xy
        rownanie = pow(int(x) - a, 2) + pow(int(y) - b, 2)
        if rownanie < pow(r, 2):
            wewnetrzne += 1
        elif rownanie == pow(r, 2):
            krawedziowe += 1
        else:
            zewnetrzne += 1
        i += 1
        if i in range(1701):
            checkpoints.append([wewnetrzne + krawedziowe, i])

for nalezace in checkpoints:
    Pk = (nalezace[0] * 400 * 400) / nalezace[1]
    pi = round((Pk / pow(r, 2)) * 10000) / 10000
    en = abs(math.pi - pi)
    przyblizenie.append([nalezace[1], en])

for x in przyblizenie:
    print(x[0], x[1])