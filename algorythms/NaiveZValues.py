def NaiveZValues(s):
    n = len(s)
    zp = [0]
    for i in range(1, n):
        j = i
        while j < n and s[j] == s[j - i]:
            j += 1
        zp.append(j - i)
    print("Массив Z-значений:", zp)


if __name__ == "__main__":
    #   Тест
    #   s = AABCAABXAAZ
    NaiveZValues(s = input('Строка:'))