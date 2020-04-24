from PositionList import PositionList
from BadCharShift import BadCharShift
from SuffixBorderArray import SuffixBorderArray
from BStoBR import BStoBR
from BStoBSM import BStoBSM
from BStoNS import BStoNS
from GoodSuffixShift import GoodSuffixShift


def BoyerMoore(pattern, text, h):
    pl = PositionList(pattern)
    m, n = len(pattern), len(text)
    bs = SuffixBorderArray(pattern)
    br = BStoBR(bs, m)
    if h:
        bs = BStoBSM(bs, m)
    nsx = BStoNS(bs, m)
    nTextR = m
    while nTextR <= n:
        k = m - 1
        i = nTextR - 1
        while k >= 0 and pattern[k] == text[i]:
            k -= 1
            i -= 1
        if k < 0:
            print("Вхождение с позиции:", i + 1)
        nShift = max(BadCharShift(pl, text[i], k), GoodSuffixShift(nsx, br, k, m))
        nTextR += nShift


if __name__ == "__main__":
    #   Тест
    #   text = abracadabra
    #   pattern = abra
    print("Алгоритм Бойера-Мура:")
    BoyerMoore(text = input('Cтрока:'), pattern = input('Подстрока:') , h = 1)