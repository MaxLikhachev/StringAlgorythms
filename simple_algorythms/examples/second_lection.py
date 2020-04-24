from string_algorithms.first_second_third import prefix_border_array, open_file


def suffix_border_array(s):
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


def prefix_border_array_modified(s, bp):
    n = len(s)
    bpm = [0 for i in range(n)]
    bpm[n - 1] = bp[n - 1]
    for i in range(0, n - 1):
        if bp[i] and s[bp[i]] == s[i + 1]:
            bpm[i] = bpm[bp[i] - 1]
        else:
            bpm[i] = bp[i]
    print('Модифицированный массив граней', bpm)
    return bpm


def bp_to_bpm(bp, n):
    bpm = [0 for i in range(n)]
    bpm[n - 1] = bp[n - 1]
    for i in range(1, n - 1):
        if bp[i] and bp[i] + 1 == bp[i + 1]:
            bpm[i] = bpm[bp[i] - 1]
        else:
            bpm[i] = bp[i]
    return bpm


def bpm_to_bp(bpm, n):
    bp = [0 for i in range(n)]
    bp[n - 1] = bpm[n - 1]
    for i in range(n - 2, -1, -1):
        bp[i] = max(bp[i + 1] - 1, bpm[i])
    print("Преобразование ВРМ в ВР", bp)


def bs_to_bsm(bs, n):
    bsm = [0 for i in range(n)]
    bsm[0] = bs[0]
    for i in range(n - 2, 0, -1):
        if bs[i] and bs[i] + 1 == bs[i - 1]:
            bsm[i] = bsm[n - bs[i]]
        else:
            bsm[i] = bs[i]
    return bsm


def bsm_to_bs(bsm, n):
    bs = [0 for i in range(n)]
    bs[0] = bsm[0]
    for i in range(1, n - 1):
        bs[i] = max(bs[i - 1] - 1, bsm[i])
    return bs


if __name__ == '__main__':
    input_line = open_file()
    print("Исходная строка", input_line.upper())
    bs = suffix_border_array(input_line)
    print('Массив граней суффиксов', bs)
    bp = prefix_border_array(input_line)
    bpm = prefix_border_array_modified(input_line, bp)
    print("Преобразование BP в BPM без S", bp_to_bpm(bp, len(input_line)))
    bsm = bs_to_bsm(bs, len(input_line))
    print("Преобразование BS в BSM", bsm)
    print("Преобразование BSM в BS", bsm_to_bs(bsm, len(input_line)))
