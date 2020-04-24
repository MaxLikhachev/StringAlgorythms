from PositionList import PositionList
from BadCharShift import BadCharShift


def BoyerMoore(pattern, text):
    pl = PositionList(pattern)
    m, n = len(pattern), len(text)
    nTextR = m
    while nTextR <= n:
        i = nTextR - 1
        k = m - 1
        while k >= 0 and pattern[k] == text[i]:
            k -= 1
            i -= 1
        if k < 0:
            print("Вхождение с позиции:", i + 1)
        nTextR += BadCharShift(pl, text[i], k)


if __name__ == "__main__":
    #   Тест
    #   text = abracadabra
    #   pattern = abra
    print("Алгоритм Бойера-Мура:")
    BoyerMoore(text = input('Cтрока:'), pattern = input('Подстрока:'))