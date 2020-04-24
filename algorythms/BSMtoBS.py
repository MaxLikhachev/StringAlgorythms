from SuffixBorderArrayModified import SuffixBorderArrayModified


def BSMtoBS(bsm, n):
    bs = [0 for i in range(n)]
    bs[0] = bsm[0]
    for i in range(1, n - 1):
        bs[i] = max(bs[i - 1] - 1, bsm[i])
    return bs


if __name__ == "__main__":
    #   Тест
    #   s = ABAAABAСBСAABAAAB
    s = input('Строка:')
    print("Преобразование BSM в BS:", BSMtoBS(SuffixBorderArrayModified(s), len(s)))