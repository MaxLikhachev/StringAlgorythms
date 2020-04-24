from string_algorithms.first_second_third import open_file, prefix_border_array
from string_algorithms.second_lection import bp_to_bpm


def kmp(pattern, text):
    m = len(pattern)
    n = len(text)
    k = 0
    pattern_bpm = bp_to_bpm(prefix_border_array(pattern), m)
    for i in range(n):
        while k and pattern[k] != text[i]:
            k = pattern_bpm[k - 1]
        if pattern[k] == text[i]:
            k += 1
        if k == m:
            print("Вхождение с позиции", i - k + 1)
            k = pattern_bpm[k - 1]


def position_list(s):
    m = len(s)
    offset_table = {}
    for i in range(256):
        offset_table[chr(i)] = m
    for i in range(m - 1, -1, -1):
        if offset_table[s[i]] == m:
            offset_table[s[i]] = [i]
        else:
            offset_table[s[i]].append(i)
    return offset_table


def bad_char_shift(pl, char_bad, pos_bad):
    if pos_bad < 0:
        return 1
    n_pos = -1  # искомая позиция слева от плохого символа char_bad
    List = pl[char_bad]
    try:
        for i in range(len(List)):
            if List[i] < pos_bad:
                n_pos = List[i]
                break
    except TypeError:
        return pos_bad - n_pos
    else:
        return pos_bad - n_pos


def BM(p, t):
    pl = position_list(p)
    m, n = len(p), len(t)
    n_text_r = m
    while n_text_r <= n:
        i = n_text_r - 1
        k = m - 1
        while k >= 0 and p[k] == t[i]:
            k -= 1
            i -= 1
        if k < 0:
            print("Вхождение с позиции", i + 1)
        n_text_r += bad_char_shift(pl, t[i], k)


if __name__ == '__main__':
    input_line = open_file()
    print("Исходная строка", input_line.upper())
    p = input("Введите подстроку: ")
    print("KMP")
    kmp(p, input_line)
    print("BM")
    BM(p, input_line)
