def ValGrow(nArr, n, nPos, nVal):
    nSeqLen = 0
    while nPos < n and nArr[nPos] == nVal:
        nSeqLen += 1
        nPos += 1
        nVal += 1
    return nSeqLen


