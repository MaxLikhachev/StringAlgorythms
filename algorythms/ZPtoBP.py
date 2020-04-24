from PrefixZValues import PrefixZValues


def ZPtoBP(zp, n):
    bp = [0] * n
    for j in range(1, n):
        for i in range(j + zp[j] - 1, j, -1):
            if bp[i]:
                break
            bp[i] = i - j + 1
    return bp


if __name__ == "__main__":
    #   Тест
    #   s = CACZZZCACA
    s = input('Строка:')
    print("Преобразование ZP в BP:", ZPtoBP(PrefixZValues(s), len(s)))