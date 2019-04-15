f = open("Dane_PR2/binarne.txt", "r")
c = f.readlines()
najwieksza = 0
for x in c:
    dx = int(x, 2)
    if dx < 65535:
        if dx > najwieksza:
            najwieksza = dx
print(najwieksza, bin(najwieksza)[2:])
