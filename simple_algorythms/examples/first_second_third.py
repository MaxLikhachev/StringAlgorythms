import os.path


def open_file():
    while 1:
        try:
            file = input("Введите имя файла с расширением: ")
            if not os.path.exists(file):
                raise FileNotFoundError(file)
            break
        except FileNotFoundError:
            print("Файла с таким именем не существует")
    with open(file, 'r') as input_string:
        in_line = ''
        for line in input_string:
            for letter in line:
                if letter is '\n':
                    continue
                in_line += letter
    return in_line


def search(input_l, substring_line):
    n = len(input_l)
    m = len(substring_line)
    count = 0
    for i in range(n - m + 1):
        j = 0
        while j < m and substring_line[j] == input_l[i + j]:
            j = j + 1
        if j == m:
            print('Найдено вхождение в позиции', i)
            count = count + 1
    print()
    return count


def naive_max_border(s):
    br = []
    for i in range(len(s) - 1, not len(br) and 0, -1):
        j = 0
        while j < i and s[j] == s[len(s) - i + j]:
            j = j + 1
        if j == i:
            br.append(s[:i])
    print('Наибольшая грань', max(br), '\n')


def prefix_border_array(s):
    n = len(s)
    bp = [0]
    for i in range(1, n):
        bp_right = bp[i-1]
        while bp_right and s[i] != s[bp_right]:
            bp_right = bp[bp_right - 1]
        if s[i] == s[bp_right]:
            bp.append(bp_right + 1)
        else:
            bp.append(0)
    return bp


if __name__ == '__main__':
    input_line = open_file()
    print("Исходная строка", input_line.upper())
    searched = input("Подстрока: ")
    print()
    result = search(input_line, searched)
    if result is 0:
        print("Нет вхождений\n")
    naive_max_border(input_line)
    print("Массив граней", prefix_border_array(input_line))
