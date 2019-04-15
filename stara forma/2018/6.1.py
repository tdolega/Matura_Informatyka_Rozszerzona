f = open("Dane_PR2/slowa.txt", "r")
c = f.readlines()
i = 0
for x in c:
    x1, x2 = x.split(" ")
    if x1[-1] == "A":
        i += 1
    if x2[-2] == "A":
        i += 1
print(i)
