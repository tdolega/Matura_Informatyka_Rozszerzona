def sd(n):
    suma = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            suma += i
    return suma


a = 75
b = sd(a) - 1
if a + 1 == sd(b):
    print(b)
else:
    print("NIE")
