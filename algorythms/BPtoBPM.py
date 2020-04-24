from PrefixBorderArray import PrefixBorderArray


def BPtoBPM(bp, n):
    bpm = [0 for i in range(n)]
    bpm[n - 1] = bp[n - 1]
    for i in range(1, n - 1):
        if bp[i] and bp[i] + 1 == bp[i + 1]:
            bpm[i] = bpm[bp[i] - 1]
        else:
            bpm[i] = bp[i]
    return bpm


if __name__ == "__main__":
    #   Тест
    #   s = ABAAABAСBСAABAAAB
    s = input('Строка:')
    print("Преобразование BP в BPM без S:", BPtoBPM(PrefixBorderArray(s), len(s)))