def Gorner2Mod(s, m, q):
    res = 0
    for i in range(m):
        res = (res << 1 + ord(s[i])) % q
    return res