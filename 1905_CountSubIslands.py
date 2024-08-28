grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]


def countSubIslands(grid1: list[list[int]], grid2: list[list[int]]) -> int:
    iles_grid1 = []
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            

print(countSubIslands(grid1, grid2))