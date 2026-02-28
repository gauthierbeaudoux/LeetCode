from math import factorial, comb

def getRow(rowIndex: int) -> list[int]:
    res = []
    
    for i in range(rowIndex+1):
        nb = comb(rowIndex, i)
        res.append(nb)
        
    return res


rowIndex = 3
print(getRow(rowIndex))