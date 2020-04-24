from STArc import STArc
from STNode import STNode
from STFindArc import STFindArc
from STArcInit import STArcInit
from STVertInit import STVertInit
from STLeavesTraversal import STLeavesTraversal


def STBuildNaive(str):
    pTree = STVertInit() # Корень дерева и его начальная дуга
    n = len(str)
    STArcInit(pTree, str[0], 0, n - 1, None, 0);

    for i in range(1, n-1): # "Поиск" очередного суффикса на дереве
        idxSuff = idxArc = 0
        pUVArc, idxSuff, idxArc = STFindArc(str, str[i], n - i, pTree, idxSuff, idxArc)
        pWNode = STNode() # Вершина-источник дуги для нового суффикса

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


if __name__ == "__main__":
    str = 'abracadabra$'
    pTree = STBuildNaive(str)
    print('Строка:', str)
    print('Суффиксное дерево:')
    print(pTree)
    print('Обход дочерних листьев:')
    for arc in pTree.arcs: 
        STLeavesTraversal(arc) 
