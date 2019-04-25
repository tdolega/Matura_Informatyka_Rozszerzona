def rnwd_wikipedia(a, b):
    x = 1
    y = 0
    r = 0
    s = 1
    while b != 0:
        modulo = a % b
        dzielenie = int(a / b)
        a = b
        b = modulo
        rp = r
        sp = s
        r = x - dzielenie * rp
        s = y - dzielenie * sp
        x = rp
        y = sp
    return a, x, y


def rnwd_matura(a, b):
    if b == 0:
        return 1, 0
    r = a % b
    x, y = rnwd_matura(b, r)
    return y, x-int(a/b)*y


print(rnwd_wikipedia(231, 30))
print(rnwd_matura(231, 30))