t = [[1]]
for i in range(1, 30):
    pt = t[i - 1]
    nt = [1]
    for j in range(1, len(pt)):
        nt.append(pt[j - 1] + pt[j])
    nt.append(1)
    t.append(nt)

print("a)")
print("max 10:", max(t[9]))
print("max 20:", max(t[19]))
print("max 30:", max(t[29]))

print("b)")
for i in range(len(t)):
    d = 0
    for x in t[i]:
        d += len(str(x))
    print(i + 1, d)

print("c)")
for i in range(len(t)):
    niepodzielne = True
    for x in t[i]:
        if x % 5 == 0:
            niepodzielne = False
    if niepodzielne:
        print(i + 1)

print("d)")
for y in range(len(t)):
    for x in range(len(t[y])):
        if t[y][x] % 3 == 0:
            t[y][x] = "X"
        else:
            t[y][x] = " "
[print(*x) for x in t]
