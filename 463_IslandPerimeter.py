grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]


def islandPerimeter(grid: list[list[int]]) -> int:
    nb_lignes = len(grid)
    nb_col = len(grid[0])
    result = 0
    for i in range(nb_lignes):
        for j in range(nb_col):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    result += 1
                if i == nb_lignes-1 or grid[i+1][j] == 0:
                    result += 1
                if j == 0 or grid[i][j-1] == 0:
                    result += 1
                if j == nb_col-1 or grid[i][j+1] == 0:
                    result += 1
    return result


print(islandPerimeter(grid))