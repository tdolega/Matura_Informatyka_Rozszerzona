f = open("Dane_PR2/binarne.txt", "r")
c = f.readlines()
i = 0
najdluzszy = ""
for x in c:
    x = x[:-1]
    x1, x2 = x[:int(len(x)/2)], x[int(len(x)/2):]
    if x1 == x2:
        i += 1
        if len(x) > len(najdluzszy):
            najdluzszy = x
print(i, najdluzszy, len(najdluzszy))
