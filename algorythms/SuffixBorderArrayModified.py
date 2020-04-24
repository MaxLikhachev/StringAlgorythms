from SuffixBorderArray import SuffixBorderArray

def SuffixBorderArrayModified(s):
    bp = SuffixBorderArray(s)
    n = len(s)
    bpm = [0 for i in range(n)]
    bpm[n - 1] = bp[n - 1]
    for i in range(0, n - 1):
        if bp[i] and s[bp[i]] == s[i + 1]:
            bpm[i] = bpm[bp[i] - 1]
        else:
            bpm[i] = bp[i]
    print('Модифицированный массив граней:', bpm)
    return bpm


if __name__ == "__main__":
    #   Тест
    #   s = ABAAABAСBСAABAAAB
    print("Массив граней суффиксов:", SuffixBorderArrayModified(s = input('Строка:')))