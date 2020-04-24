def BStoNS(bs, m):
    ns = [-1] * m
    for j in range(m):
        if bs[j]:
            k = m - bs[j] - 1
            ns[k] = j
    return ns