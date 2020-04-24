class STArc:
    def __init__(self, iBeg = 0, iEnd = 0, pDestVert = None, iDestVert = 0):
        self.iBeg = iBeg
        self.iEnd = iEnd # Индексы символов метки (в исходной строке) 
        self.pDestVert = pDestVert # Вершина, куда входит дуга (для листа = NULL)
        self.iDestVert = iDestVert # Индекс листа, куда входит дуга (для внутренней = -1)

    def __str__(self):
        return '(' + self.iBeg.__str__() + ', ' + self.iEnd.__str__() + ') -> ' + self.iDestVert.__str__()  + ' ---> ' + self.pDestVert.__str__() + '\n'
