grid = [[0,1,1],[1,0,1],[0,0,1]]

def onesMinusZeros(grid: list[list[int]]) -> list[list[int]]:
    result = []
    nb_row = len(grid)
    nb_col = len(grid[0])
    one_col = {}
    zero_col = {}
    for i in range(nb_row):
        one_row = sum(grid[i])
        zero_row = nb_col - one_row
        list_temp = []
        for j in range(nb_col):
            if i == 0:
                one_col[j] = sum(row[j] for row in grid)
                zero_col[j] = nb_row - one_col[j]
            list_temp.append(one_row +  one_col[j] - zero_row - zero_col[j])
        result.append(list_temp)
    return result


print(onesMinusZeros(grid))