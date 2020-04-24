def PositionList(s):
    m = len(s)
    offsetTable = {}
    for i in range(256):
        offsetTable[chr(i)] = m
    for i in range(m - 1, -1, -1):
        if offsetTable[s[i]] == m:
            offsetTable[s[i]] = [i]
        else:
            offsetTable[s[i]].append(i)
    return offsetTable

if __name__ == "__main__":
    #   Тест
    #   s = CACZZZCACA
    print("Список позиций:", PositionList(s = input('Строка:')))