with open("Dane_PR2/liczby.txt", "r") as o:
    c = [int(x, 2) for x in o.readlines()]
    print("min:", c.index(min(c))+1, ", max:", c.index(max(c))+1)

# EZ 6 pkt, pozdro dla tych co wybrali C++
