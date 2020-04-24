def GoodSuffixShift(nsx, br, posBad, m):
    if posBad == m - 1:
        return 1
    if posBad < 0:
        return m - br[0]
    copyPos = nsx[posBad]
    if copyPos >= 0:
        shift = posBad - copyPos + 1
    else:
        shift = m - br[posBad]
    return shift
