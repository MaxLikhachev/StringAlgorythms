from STArc import STArc
from STchArcIdx import STchArcIdx

def STArcInit(pSNode, chArcIdx, iBeg, iEnd, pDestVert, iDestVert):
    pArc = STArc()
    pArc.iBeg = iBeg
    pArc.iEnd = iEnd
    pSNode.arcs[STchArcIdx(chArcIdx)] = pArc
    pArc.pDestVert = pDestVert
    pArc.iDestVert = iDestVert
    return pArc