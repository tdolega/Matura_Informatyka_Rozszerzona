with open("Dane_PR2/dane.txt", "r") as o:
    content = o.readlines()
    liniiDoUsuniecia = 0
    for y in content:
        x = y.split(" ")
        for i in range(160):
            if int(x[i]) != int(x[319-i]):
                liniiDoUsuniecia += 1
                break
    print(liniiDoUsuniecia)
