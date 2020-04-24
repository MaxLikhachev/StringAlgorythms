from string_algorithms.second_lection import suffix_border_array, open_file, bs_to_bsm
from string_algorithms.fourth_lection import position_list, bad_char_shift


def bs_to_ns(bs, m):
    ns = [-1] * m
    for j in range(m):
        if bs[j]:
            k = m - bs[j] - 1
            ns[k] = j
    return ns


def bs_to_br(bs, m):
    br = [0]*m
    curr_border = bs[0]
    k = 0
    while curr_border:
        for k in range(m - curr_border):
            br[k] = curr_border
        curr_border = bs[k + 1]
    return br


def good_suffix_shift(nsx, br, pos_bad, m):
    if pos_bad == m - 1:
        return 1
    if pos_bad < 0:
        return m - br[0]
    copy_pos = nsx[pos_bad]
    if copy_pos >= 0:
        shift = pos_bad - copy_pos + 1
    else:
        shift = m - br[pos_bad]
    return shift


def BM(p, t, h):
    pl = position_list(p)
    m, n = len(p), len(t)
    bs = suffix_border_array(p)
    br = bs_to_br(bs, m)
    if h:
        bs = bs_to_bsm(bs, m)
    nsx = bs_to_ns(bs, m)
    print(nsx)
    n_text_r = m
    while n_text_r <= n:
        k = m - 1
        i = n_text_r - 1
        while k >= 0 and p[k] == t[i]:
            k -= 1
            i -= 1
        if k < 0:
            print("Вхождение с позиции", i + 1)
        n_shift = max(bad_char_shift(pl, t[i], k), good_suffix_shift(nsx, br, k, m))
        n_text_r += n_shift


def gorner_2_mod(s, m, q):
    res = 0
    for i in range(m):
        res = (res << 1 + ord(s[i])) % q
    return res


def KR(p, t, q):
    m, n = len(p), len(t)
    p2m = 1
    for i in range(m - 1):
        p2m = (p2m << 1) % q
    hp = gorner_2_mod(p, m, q)
    ht = gorner_2_mod(t, m, q)
    for j in range(n - m + 1):
        if ht == hp:
            k = 0
            while k < m and p[k] == t[j+k]:
                k += 1
            if k == m:
                print("Вхождение с позиции", j)
        try:
            ht = ((ht - p2m * ord(t[j])) << 1 + ord(t[j+m])) % q
        except IndexError:
            pass
        if ht < 0:
            ht += q


if __name__ == '__main__':
    input_line = open_file()
    print("Исходная строка", input_line.upper())
    p = input("Введите подстроку: ")
    print("Алгоритм Бойера-Мура")
    BM(p, input_line, 1)
    print("Алгоритм Карпа-Рабина")
    KR(p, input_line, 2)
