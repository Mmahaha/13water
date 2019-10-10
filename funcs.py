def reversed_cmp(x, y):
    if x[1]=='1' and y[1]<='9' and y[1]>='2':
        return 1
    if y[1]=='1' and x[1]<='9' and x[1]>='2':
        return -1
    if x[1]=='A':
        return 1
    if y[1]=='A':
        return -1
    if x[1]=='Q':
        if y[1]!='K' and y[1]!='A':
            return 1
        else:
            return -1
    if y[1]=='Q':
        if x[1]!='K' and x[1]!='A':
            return -1
        else:
            return 1
   
    if x[1] > y[1]:
        return 1
    if x[1] < y[1]:
        return -1
    return 0


