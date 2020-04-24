from SuffixBorderArray import SuffixBorderArray


def BStoBSM(bs, n):
    bsm = [0 for i in range(n)]
    bsm[0] = bs[0]
    for i in range(n - 2, 0, -1):
        if bs[i] and bs[i] + 1 == bs[i - 1]:
            bsm[i] = bsm[n - bs[i]]
        else:
            bsm[i] = bs[i]
    return bsm


if __name__ == "__main__":
    #   Тест
    #   s = ABAAABAСBСAABAAAB
    s = input('Строка:')
    print("Преобразование BS в BSM:", BStoBSM(SuffixBorderArray(s), len(s)))