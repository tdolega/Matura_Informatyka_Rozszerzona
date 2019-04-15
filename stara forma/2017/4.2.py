f = open("Dane_PR2/binarne.txt", "r")
c = f.readlines()
bledne = 0
najmniejsze = 99999  # xd
for x in c:
    x = x[:-1]
    bcd = [x[i:i + 4] for i in range(0, len(x), 4)]
    for y in bcd:
        if int(y, 2) > 9:
            bledne += 1
            if len(x) < najmniejsze:
                najmniejsze = len(x)
            break
print(bledne, najmniejsze)
