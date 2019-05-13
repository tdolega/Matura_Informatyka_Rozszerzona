def f43(x):
    for char1 in x[:-1]:
        for char2 in x[:-1]:
            if abs(ord(char1) - ord(char2)) > 10:
                return False
    return x[:-1]


with open("Dane_PR2/sygnaly.txt", "r") as o:
    for x in o.readlines():
        if f43(x):
            print(f43(x))
