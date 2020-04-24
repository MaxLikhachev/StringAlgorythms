from Gorner2Mod import Gorner2Mod


def KarpRabin(pattern, text, q):
    m, n = len(pattern), len(text)
    p2m = 1
    for i in range(m - 1):
        p2m = (p2m << 1) % q
    hp = Gorner2Mod(pattern, m, q)
    ht = Gorner2Mod(text, m, q)
    for j in range(n - m + 1):
        if ht == hp:
            k = 0
            while k < m and pattern[k] == text[j + k]:
                k += 1
            if k == m:
                print("Вхождение с позиции", j)
        try:
            ht = ((ht - p2m * ord(text[j])) << 1 + ord(text[j + m])) % q
        except IndexError:
            pass
        if ht < 0:
            ht += q


if __name__ == "__main__":
    #   Тест
    #   text = abracadabra
    #   pattern = abra
    print("Алгоритм Карпа-Рабина:")
    KarpRabin(text = input('Cтрока:'), pattern = input('Подстрока:') , q = 2)