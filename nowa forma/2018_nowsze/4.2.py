with open("Dane_PR2/sygnaly.txt", "r") as o:
    topSlowo = ["", 0]
    for x in o.readlines():
        x = x[:-1]
        litery = []
        for y in x[:-1]:
            if y not in litery:
                litery.append(y)
        if len(litery) > topSlowo[1]:
            topSlowo = [x, len(litery)]
    print(*topSlowo)
