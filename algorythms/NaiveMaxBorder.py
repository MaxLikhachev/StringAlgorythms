def NaiveMaxBorder(s):
    br = []
    for i in range(len(s) - 1, not len(br) and 0, -1):
        j = 0
        while j < i and s[j] == s[len(s) - i + j]:
            j = j + 1
        if j == i:
            br.append(s[:i])
    print('Наибольшая грань:', max(br), '\n')

if __name__ == "__main__":
    #   Тест
    #   s = ABAABABAABAAB
    NaiveMaxBorder(s = input('Строка:'))