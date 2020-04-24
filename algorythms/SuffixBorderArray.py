def SuffixBorderArray(s):
    n = len(s)
    bs = [0 for i in range(n)]
    for i in range(n - 2, -1, -1):
        bs_left = bs[i + 1]
        while bs_left and s[i] != s[n - bs_left - 1]:
            bs_left = bs[n - bs_left]
        if s[i] == s[n - bs_left - 1]:
            bs[i] = bs_left + 1
        else:
            bs[i] = 0
    return bs


if __name__ == "__main__":
    #   Тест
    #   s = ABAAABAСBСAABAAAB
    print("Массив граней суффиксов:", SuffixBorderArray(s = input('Строка:')))