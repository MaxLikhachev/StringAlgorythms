def ShiftAnd(p, t):
    m, n = len(p), len(t)
    chBeg, chEnd = '0', 'z'
    nA = ord(chEnd) - ord(chBeg) + 1
    B = [0] * nA
    for j in range(m):
        B[ord(p[j]) - ord(chBeg)] |= 1 << m - 1 - j
    uHigh = 1 << (m - 1)
    M = 0
    for i in range(n):
        M = (M >> 1 | uHigh) & B[ord(t[i]) - ord(chBeg)]
        if M & 1:
            print("Вхождение с позиции:", i - m + 1)


if __name__ == "__main__":
    #   Тест
    #   T = abracadabra
    #   P = abra 
    ShiftAnd(t = input("Cтрока:"), p = input("Подстрока:"))

