def BadCharShift(pl, charBad, posBad):
    if posBad < 0:
        return 1
    nPos = -1  # искомая позиция слева от плохого символа charBad
    List = pl[charBad]
    try:
        for i in range(len(List)):
            if List[i] < posBad:
                nPos = List[i]
                break
    except TypeError:
        return posBad - nPos 
    else: 
        return posBad - nPos 