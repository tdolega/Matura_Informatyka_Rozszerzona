with open("Dane_PR2/liczby.txt", "r") as o:
    content = o.readlines()
    przez2 = 0
    przez8 = 0
    for liczba in content:
        if liczba[-2] == "0":
            przez2 += 1
            if liczba[-4:-1] == "000":
                przez8 += 1
    print("2:", przez2,", 8:", przez8)
