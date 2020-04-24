from STnAlpha import STnAlpha
from STArc import STArc


class STNode:
    def __init__(self, arcs = [], nAlpha = STnAlpha()): # Массив ссылок на исходящие дуги
        self.arcs = [STArc() for i in range(0, nAlpha)] # nAlpha – длина алфавита

    def __str__(self):
        return ''.join([chr(ord('a') + i) + ' :: ' + self.arcs[i].__str__() for i in range(0, STnAlpha())])    
