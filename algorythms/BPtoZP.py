from PrefixBorderArray import PrefixBorderArray
from ValGrow import ValGrow


def BPtoZP(bp, n):
    l, r = 0, 0
    zp = [0] * n
    for i in range(1, n):
        if i >= r:
            zp[i] = ValGrow(bp, n, i, 1)
            l = i
            r = l + zp[i]
        else:
            j = i - l
            if zp[j] < r - i:
                zp[i] = zp[j]
            else:
                zp[i] = r - i + ValGrow(bp, n, r, r - i - 1)
                l = i
                r = l + zp[i]
    return zp


if __name__ == "__main__":
    #   Тест
    #   s = CACZZZCACA
    s = input('Строка:')
    print("Преобразование BP в ZP:", BPtoZP(PrefixBorderArray(s), len(s)))