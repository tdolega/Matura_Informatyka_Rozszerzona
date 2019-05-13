with open("Dane_PR2/dane.txt", "r") as o:
    linie = [int(x) for l in [x.split(" ") for x in o.readlines()] for x in l]
    print(max(linie), min(linie))
