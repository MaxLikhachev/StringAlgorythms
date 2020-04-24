def NaiveStringMatch(string, substring):
    n = len(string)
    m = len(substring)
    count = 0
    for i in range(n - m + 1):
        j = 0
        while j < m and substring[j] == string[i + j]:
            j = j + 1
        if j == m:
            print('Найдено вхождение в позиции:', i)
            count = count + 1
    print()
    return count


if __name__ == "__main__":
    NaiveStringMatch(string = input('Строка:'), substring = input('Подстрока:'))