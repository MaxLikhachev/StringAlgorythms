from STArc import STArc
from STchArcIdx import STchArcIdx


def STFindArc(str, substr, m, pTree, idxSubstr, idxArc):
    pArc = STArc() # Дуга, на которой остановится поиск
    idxSubstr = idxArc = 0; # Индексы несовпавших символов
    pCurrNode = pTree; # Начинаем движение от корня
    bStopped = 0;
    while (not bStopped and pCurrNode): # Поиск подстроки по меткам дуг – вычисления
        pNextArc = pCurrNode.arcs[STchArcIdx(substr[idxSubstr])] 

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
