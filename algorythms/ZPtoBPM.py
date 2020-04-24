from PrefixZValues import PrefixZValues


def ZPtoBPM(zp, n):
    bpm = [0 for i in range(n)]
    for j in range(n - 1, 0, -1):
        i = j + zp[j] - 1
        bpm[i] = zp[j]
    return bpm


if __name__ == "__main__":
    #   Тест
    #   s = AABCAABXAAZ
    s = input('Строка:')
    print("Преобразование ZP в BPM:", ZPtoBPM(PrefixZValues(s), len(s)))