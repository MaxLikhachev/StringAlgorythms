from PrefixBorderArray import PrefixBorderArray
from BPtoBPM import BPtoBPM


def KnuthMorrisPratt(pattern, text):
    m = len(pattern)
    n = len(text)
    k = 0
    patternBPM = BPtoBPM(PrefixBorderArray(pattern), m)
    for i in range(n):
        while k and pattern[k] != text[i]:
            k = patternBPM[k - 1]
        if pattern[k] == text[i]:
            k += 1
        if k == m:
            print("Вхождение с позиции:", i - k + 1)
            k = patternBPM[k - 1]


if __name__ == "__main__":
    #   Тест
    #   s = CACZZZCACA
    s = input('Строка:')
    print("Алгоритм Кнута-Морриса-Пратта:", KnuthMorrisPratt(PrefixBorderArray(s), len(s)))