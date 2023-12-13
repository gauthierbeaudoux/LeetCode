mat = [[1,0,0],[0,0,1],[1,0,0]]

def numSpecial(mat: list[list[int]]) -> int:
    result = 0
    list_col = [i for i in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in list_col:
            if mat[i][j] == 1:
                list_col.remove(j)
                if sum(mat[i]) == 1 and sum(row[j] for row in mat) == 1:
                    result += 1
                break
    return result


print(numSpecial(mat))