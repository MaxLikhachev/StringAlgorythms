from PrefixBorderArrayModified import PrefixBorderArrayModified


def BPMtoBP(bpm, n):
    bp = [0 for i in range(n)]
    bp[n - 1] = bpm[n - 1]
    for i in range(n - 2, -1, -1):
        bp[i] = max(bp[i + 1] - 1, bpm[i])
    return bp


if __name__ == "__main__":
    #   Тест
    #   s = ABAAABAСBСAABAAAB
    s = input('Строка:')
    print("Преобразование BPM в BP без S:", BPMtoBP(PrefixBorderArrayModified(s), len(s)))