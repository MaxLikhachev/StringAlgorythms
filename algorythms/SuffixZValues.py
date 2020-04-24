from StrCompBack import StrCompBack


def SuffixZValues(s):
    n = len(s)
    l = r = n - 1
    zs = [0 for i in range(n)]
    for i in range(n - 2, 0, -1):
        if i <= l:
            zs[i] = StrCompBack(s, i, n - 1)
            r = i
            l = r - zs[i]
        else:
            j = n - (r + 1 - i)
            if zs[j] < i - l:
                zs[i] = zs[j]
            else:
                zs[i] = i - l + StrCompBack(s, l, n - i + l)
                r = i
                l = r - zs[i]
    print("Массив Z-значений суффиксов:", zs)


if __name__ == "__main__":
    #   Тест
    #   s = AABCAABXAAZ
    SuffixZValues(s = input('Строка:'))