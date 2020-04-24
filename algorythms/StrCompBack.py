def StrCompBack(s, i1, i2):
    eqLen = 0
    while i1 >= 0 and i2 >= 0 and s[i1-1] == s[i2-1]:
        eqLen += 1
        i1 -= 1
        i2 -= 1
    return eqLen


