MASA = [8, 4, 1, 2, 3, 5, 1]
CENA = [320, 152, 37, 70, 99, 155, 30]
n = len(MASA)
mk = 10

K = []
for i in range(n):
    K.append(0)
w = 0
i = 0
while i < n and mk > 0:
    if mk / MASA[i] >= 1:
        mk -= MASA[i]
        K[i] = 1
        w += CENA[i]
    i += 1
print(w)
