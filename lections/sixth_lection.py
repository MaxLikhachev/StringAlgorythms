from string_algorithms.first_second_third import open_file


def shift_and(p, t):
    m, n = len(p), len(t)
    ch_beg, ch_end = '0', 'z'
    nA = ord(ch_end) - ord(ch_beg) + 1
    B = [0] * nA
    for j in range(m):
        B[ord(p[j]) - ord(ch_beg)] |= 1 << m - 1 - j
    u_high = 1 << (m - 1)
    M = 0
    for i in range(n):
        M = (M >> 1 | u_high) & B[ord(t[i]) - ord(ch_beg)]
        if M & 1:
            print("Вхождение с позиции", i - m + 1)


def shift_and_fz(p, t, k):
    m, n = len(p), len(t)
    ch_beg, ch_end = '0', 'z'
    nA = ord(ch_end) - ord(ch_beg) + 1
    B = [0] * nA
    for j in range(m):
        B[ord(p[j]) - ord(ch_beg)] |= 1 << m - 1 - j
    u_high = 1 << (m - 1)
    M = [0] * (k + 1)
    M1 = [0] * (k + 1)
    for i in range(n):
        for l in range(k + 1):
            M1[l] = M[l]
            M[l] = (M[l] >> 1 | u_high) & B[ord(t[i]) - ord(ch_beg)]
            if l:
                M[l] |= M1[l - 1] >> 1 | u_high
            if l == k and M[l] & 1:
                print("Найдено вхождение ", i - m + 1)


if __name__ == '__main__':
    input_line = open_file()
    print("Исходная строка", input_line.upper())
    p = input("Введите подстроку ")
    print("ShiftAnd")
    shift_and(p, input_line)
    print("ShiftAndFz")
    k = int(input("Введите k "))
    while k >= len(p):
        k = int(input("k должно быть меньше длины подстроки "))
    shift_and_fz(p, input_line, k)
