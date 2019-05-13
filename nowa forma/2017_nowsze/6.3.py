def sprawdz(ll, x, y):
    def chck(w1, w2):
        if w1 < 0 or w1 > 199 or w2 < 0 or w2 > 319:
            return False
        if abs(int(ll[w1][w2]) - int(ll[y][x])) > 128:
            return True

    if chck(y, x - 1) or chck(y, x + 1) or chck(y - 1, x) or chck(y + 1, x):
        return 1
    return 0


with open("Dane_PR2/dane.txt", "r") as o:
    wynik = 0
    linie = [x.split(" ") for x in o.readlines()]
    for y in range(200):
        for x in range(320):
            wynik += sprawdz(linie, x, y)
    print(wynik)
