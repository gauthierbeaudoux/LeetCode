dimensions = [[9,3],[8,6]]

def areaOfMaxDiagonal(dimensions: list[list[int]]) -> int:
    result = -1
    sq_diagonale = -1
    for i in dimensions:
        sq_diago = i[0]**2 + i[1]**2
        if sq_diago > sq_diagonale:
            result = i[0]*i[1]
            sq_diagonale = sq_diago
        elif sq_diago == sq_diagonale:
            result = max(result, i[0]*i[1])
            
    
    return result


print(areaOfMaxDiagonal(dimensions))