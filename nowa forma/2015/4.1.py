with open("Dane_PR2/liczby.txt", "r") as o:
    content = o.readlines()
    wiecejZer = 0
    for liczba in content:
        zera = 0
        jedynki = 0
        for cyfra in liczba:
            if cyfra == "1":
                jedynki += 1
            if cyfra == "0":
                zera += 1
        if zera > jedynki:
            wiecejZer += 1
    print(wiecejZer)
