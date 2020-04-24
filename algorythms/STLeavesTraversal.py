from STnAlpha import STnAlpha


def STLeavesTraversal (pStartArc, STnAlpha = STnAlpha()): # pStartArc – стартовая дуга обхода; STnAlpha – длина алфавита
        if pStartArc.iDestVert >= 0: # Если дуга направлена к листу
            print("Найдена позиция:", pStartArc.iDestVert)
        else: # Дуга направлена к внутренней вершине дерева PNode 
            pStartNode = pStartArc.pDestVert
            for k in range(0, STnAlpha):   # Перебор дуг дочерней вершины
                pArc = pStartNode.arcs[k]
                if (pArc): 
                    STLeavesTraversal(pArc)