f = open("Dane_PR2/slowa.txt", "r")
c = f.readlines()
i = 0
for x in c:
    x1, x2 = x.split(" ")
    chars1, chars2 = [*x1], [*x2]
    chars1.sort()
    chars2.sort()
    if chars1 == chars2[1:]:
        i += 1
print(i)
