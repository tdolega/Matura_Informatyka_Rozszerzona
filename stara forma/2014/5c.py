with open("dane_PR/NAPIS.TXT", "r") as o:
    unikalne = []
    print(*list(filter(None, [slowo[:-1] if slowo in unikalne else unikalne.append(slowo) for slowo in o.readlines()])), sep="\n")
