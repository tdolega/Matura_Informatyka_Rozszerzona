def get_distance(c1, c2):
    dist = (ord(c2) - 65) - (ord(c1) - 65)
    if dist < 0:
        return 26 + dist
    return dist


wyniki = []
with open("Dane_PR2/dane_6_3.txt", "r") as o:
    content = o.readlines()
    for s in content:
        s1, s2 = s.split(" ")
        s2 = s2[:-1]
        dist = get_distance(s1[0], s2[0])
        for i in range(len(s1)):
            if get_distance(s1[i], s2[i]) != dist:
                wyniki.append(s1 + "\n")
                break

with open("wyniki_6_3.txt", "w") as o:
    o.writelines(wyniki)
