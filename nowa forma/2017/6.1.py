with open("Dane_PR2/dane.txt", "r") as o:
    content = o.readlines()
    pixels = []
    for y in content:
        x = y.split(" ")
        for pixel in x:
            pixels.append(int(pixel))
    print("najciemniejszy:", min(pixels))
    print("najjasniejszy:", max(pixels))
