def NAlpha(): # nAlpha – длина алфавита
    return ord('z') - ord('0') + 1

def CHArcIdx(chArcIdx): # Определение индекса (кода) символа
    return ord(chArcIdx) - ord('0')

class Arc:
    def __init__(self, iBeg = 0, iEnd = 0, pDestVert = None, iDestVert = 0):
        self.iBeg = iBeg
        self.iEnd = iEnd # Индексы символов метки (в исходной строке) 
        self.pDestVert = pDestVert # Вершина, куда входит дуга (для листа = NULL)
        self.iDestVert = iDestVert # Индекс листа, куда входит дуга (для внутренней = -1)

    # def isNone(self):
        # return True if self.pTree == 0 and self.iEnd == 0 and self.pDestVert is None and iDestVert == 0 else False

    def __str__(self):
        return '(' + self.iBeg.__str__() + ', ' + self.iEnd.__str__() + ') -> ' + self.iDestVert.__str__()  + ' ---> ' + self.pDestVert.__str__() + '\n'

# Вершина дерева
class Node:
    def __init__(self, arcs = [], nAlpha = NAlpha()): # Массив ссылок на исходящие дуги
        self.arcs = [Arc() for i in range(0, nAlpha)] # nAlpha – длина алфавита

    def __str__(self):
        return ''.join([chr(ord('a') + i) + ' :: ' + self.arcs[i].__str__() for i in range(0, NAlpha())])    

def STVertInit():
    pVert = Node()  # Заполн. нулями
    return pVert;

def STArcInit(pSNode, chArcIdx, iBeg, iEnd, pDestVert, iDestVert):
    pArc = Arc()
    pArc.iBeg = iBeg
    pArc.iEnd = iEnd
    # print('chArcIdx:', chArcIdx, ', ', CHArcIdx(chArcIdx))
    pSNode.arcs[CHArcIdx(chArcIdx)] = pArc
    pArc.pDestVert = pDestVert
    pArc.iDestVert = iDestVert
    return pArc

def FindSuffixTreeArc(str, substr, m, pTree, idxSubstr, idxArc):
    pArc = Arc() # Дуга, на которой остановится поиск
    idxSubstr = idxArc = 0; # Индексы несовпавших символов
    pCurrNode = pTree; # Начинаем движение от корня
    bStopped = 0;
    while (not bStopped and pCurrNode): # Поиск подстроки по меткам дуг – вычисления
        pNextArc = pCurrNode.arcs[CHArcIdx(substr[idxSubstr])] 

        if (pNextArc): #Есть совпадение с начальным символом метки дуги
            pArc = pNextArc
            idxArc = pArc.iBeg
            # Сравниваем последующие символы
            while idxSubstr < m and idxArc < pArc.iEnd + 1 and substr[idxSubstr] == str[idxArc] and idxSubstr < len(substr) - 1 and idxArc < len(str) - 1:
                idxSubstr += 1
                idxArc += 1
                # print(substr, idxSubstr, str, idxArc)

            if idxArc <= pArc.iEnd: 
                bStopped = 1 # Не прошли метку
            else: 
                pCurrNode = pArc.pDestVert # Переход к следующей вершине
        
        else: bStopped = 1 # Нет продолжения пути
    
    if idxSubstr == m: 
        idxArc += 1 # Чтобы idxArc было за границей совпадения
    return pArc, idxSubstr, idxArc


def STBuidNaive(str):
    pTree = STVertInit() # Корень дерева и его начальная дуга
    n = len(str)
    STArcInit(pTree, str[0], 0, n - 1, None, 0);

    for i in range(1, n-1): # "Поиск" очередного суффикса на дереве
        idxSuff = idxArc = 0
        pUVArc, idxSuff, idxArc = FindSuffixTreeArc(str, str[i], n - i, pTree, idxSuff, idxArc)
        pWNode = Node() # Вершина-источник дуги для нового суффикса

        if not pUVArc: # Поиск остановился в корне
            pWNode = pTree
        else: # Поиск остановился внутри дуги (U, V), требуется ее разделение
            if idxArc <= pUVArc.iEnd: # Новая разделяющая вершина
                pWNode = STVertInit()
                pWArc = STArcInit(pWNode, str[idxArc], idxArc, pUVArc.iEnd, pUVArc.pDestVert, pUVArc.iDestVert) # Дуга из W в V

                pUVArc.pDestVert = pWNode # Дуга из U в W
                pUVArc.iEnd = idxArc - 1
                pUVArc.iDestVert = -1
            else:   # Поиск остановился в конце дуги (U, V)
                pWNode = pUVArc.pDestVert 

            STArcInit(pWNode, str[i + idxSuff], i + idxSuff, n - 1, None, i) # Добавить новую дугу из вершины W в лист
    
    return pTree        

def STLeavesTraversal (pStartArc, nAlpha = NAlpha()): # pStartArc – стартовая дуга обхода; nAlpha – длина алфавита
        if pStartArc.iDestVert >= 0: # Если дуга направлена к листу
            print("Найдена позиция:", pStartArc.iDestVert)
        else: # Дуга направлена к внутренней вершине дерева PNode 
            pStartNode = pStartArc.pDestVert
            for k in range(0, nAlpha):   # Перебор дуг дочерней вершины
                pArc = pStartNode.arcs[k]
                if (pArc): 
                    STLeavesTraversal(pArc)


if __name__ == "__main__":
    str = 'abracadabra$'
    pTree = STBuidNaive(str)
    print('Строка:', str)
    print('Суффиксное дерево:')
    print(pTree)
    print('Обход дочерних листьев:')
    for arc in pTree.arcs: 
        STLeavesTraversal(arc) 
