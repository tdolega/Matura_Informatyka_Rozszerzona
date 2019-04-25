def jestPierwsza(l):
    for i in range(2, l // 2):
        if l % i == 0:
            return False
    return True


napisyPierwsze = 0
with open("dane_PR/NAPIS.TXT", "r") as o:
    for napis in o.readlines():
        sumaAscii = 0
        for char in napis.replace("\n", ""): # w nowych maturach prościej [:-1] ale tutaj nie ma entera na końcu pliku z zadaniem, łatwo stracić punkty
            sumaAscii += ord(char)
        if jestPierwsza(sumaAscii):
            napisyPierwsze += 1
print(napisyPierwsze)
