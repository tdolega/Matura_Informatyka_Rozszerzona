with open("Dane_PR2/sygnaly.txt") as o:
    content = o.readlines()
    result = ""
    for i in range(39, 1000, 40):
        result += content[i][9]
    print(result)
