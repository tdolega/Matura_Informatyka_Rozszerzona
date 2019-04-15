f = open("Dane_PR2/slowa.txt", "r")
c = f.readlines()
i = 0
for x in c:
    x1, x2 = x.split(" ")
    if x1 in x2:
        i += 1
print(i)
