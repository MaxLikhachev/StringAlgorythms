from StrComp import StrComp


def PrefixZValues(s):
    n = len(s)
    l, r = 0, 0
    zp = [0] * n
    for i in range(1, n):
        # zp.append(0)
        if i >= r:
            zp[i] = StrComp(s, n, 0, i)
            l = i
            r = l + zp[i]
        else:
            j = i - l
            if zp[j] < r - i:
                zp[i] = zp[j]  # так как мы находимся в подстроке, совпадающей с префиксом всей строки
            else:
                zp[i] = r - i + StrComp(s, n, r - i, r)
                l = i
                r = l + zp[i]
    print("Массив Z-значений:", zp)
    return zp


if __name__ == "__main__":
    #   Тест
    #   s = AABCAABXAAZ
    PrefixZValues(s = input('Строка:'))