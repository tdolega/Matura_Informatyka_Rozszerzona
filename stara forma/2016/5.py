listaLinijek = []


def start():
    listaLinijek = []
    f = open("./Dane_PR2/gra.txt", "r")
    o = f.readlines()
    for linijka in o:
        linijka = linijka[:-1]
        listaLinijek.append(list(linijka))
    return listaLinijek


def sprawdz(ll, x3, y3, wysokosc, szerokosc):
    if (x3 > szerokosc):
        x3 = 0
    if (y3 > wysokosc):
        y3 = 0
    if ll[y3][x3] == "X":
        return 1
    return 0


def sprawdz_ile_sasiadow(ll, x1, y1, wysokosc, szerokosc):
    iloscSasiadow = 0
    for x2 in range(x1 - 1, x1 + 2):
        for y2 in range(y1 - 1, y1 + 2):
            if (x2 == x1) and (y2 == y1):
                continue
            iloscSasiadow += sprawdz(ll, x2, y2, wysokosc, szerokosc)
    return iloscSasiadow


def kolejne_pokolenie(ll):
    nowa_ll = [wewLista[:] for wewLista in ll]
    wysokosc, szerokosc = len(ll) - 1, len(ll[0]) - 1
    for y in range(wysokosc + 1):
        for x in range(szerokosc + 1):
            iloscSasiadow = sprawdz_ile_sasiadow(ll, x, y, wysokosc, szerokosc)
            nowa_ll[y][x] = iloscSasiadow
            if ll[y][x] == "." and iloscSasiadow == 3:
                nowa_ll[y][x] = "X"
            elif ll[y][x] == "X" and (iloscSasiadow == 2 or iloscSasiadow == 3):
                nowa_ll[y][x] = "X"
            else:
                nowa_ll[y][x] = "."
    return nowa_ll


def zywe_komorki(ll):
    i = 0
    for y3 in range(len(ll)):
        for x3 in range(len(ll[0])):
            if ll[y3][x3] == "X":
                i += 1
    return i


def symulacja(iloscPokolen):
    global listaLinijek
    listaLinijek = start()
    for pokolenie in range(iloscPokolen - 1):
        kolejnePokolenie = kolejne_pokolenie(listaLinijek)
        # print("pokolenie", pokolenie + 2)
        # for pok in kolejnePokolenie:
        #     print(pok)
        listaLinijek = kolejnePokolenie
    return listaLinijek


def zadanie51():
    global listaLinijek
    symulacja(37)
    wiersz = 2
    kolumna = 19
    return sprawdz_ile_sasiadow(listaLinijek, kolumna - 1, wiersz - 1, 11, 19)


def zadanie52():
    global listaLinijek
    symulacja(2)
    return zywe_komorki(listaLinijek)


def zadanie53():
    global listaLinijek
    zapisy_symulacji = []
    # nieoptymalne
    for i in range(100):
        zapisy_symulacji.append(symulacja(i))
        if zapisy_symulacji[i] == zapisy_symulacji[i - 1] and i > 2:
            return [i, zywe_komorki(listaLinijek)]


print("zadanie 5.1)", zadanie51())
print("zadanie 5.2)", zadanie52())
print("zadanie 5.3)", zadanie53())
