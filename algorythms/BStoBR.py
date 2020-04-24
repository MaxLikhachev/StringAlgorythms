def BStoBR(bs, m):
    br = [0] * m
    currBorder = bs[0]
    k = 0
    while currBorder:
        for k in range(m - currBorder):
            br[k] = currBorder
        currBorder = bs[k + 1]
    return br