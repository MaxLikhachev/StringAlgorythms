def PrefixBorderArray(s):
    n = len(s)
    bp = [0]
    for i in range(1, n):
        bpRight = bp[i-1]
        while bpRight and s[i] != s[bpRight]:
            bpRight = bp[bpRight - 1]
        if s[i] == s[bpRight]:
            bp.append(bpRight + 1)
        else:
            bp.append(0)
    return bp


if __name__ == "__main__":
    #   Тест
    #   s = ABAAABAСBСAABAAAB
    print("Массив граней:", PrefixBorderArray(s = input('Строка:')))