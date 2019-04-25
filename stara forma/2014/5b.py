def czy_rosnoca(tekst):
    for i in range(len(tekst) - 1):
        poprzednia = ord(tekst[i])
        if ord(tekst[i + 1]) <= poprzednia:
            return False
    return True


with open("dane_PR/NAPIS.TXT", "r") as o:
    for napis in o.readlines():
        napis = napis.replace("\n", "")
        if czy_rosnoca(napis):
            print(napis)
