def StrComp(s, n, i1, i2):
    eqLen = 0
    while i1 < n and i2 < n and s[i1] == s[i2]:
        eqLen += 1
        i1 += 1
        i2 += 1
    return eqLen

