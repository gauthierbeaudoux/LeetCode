grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]


def countNegatives(grid: list[list[int]]) -> int:
    result = 0
    ligne = 0
    colonne = len(grid[0])-1
    nb_lignes = len(grid)
    nb_col = len(grid[0])
    
    while colonne >= 0:
        while ligne < nb_lignes and grid[ligne][colonne] >= 0:
            ligne += 1
        else:
            result += (nb_lignes - ligne)
        colonne -= 1

    return result


print(countNegatives(grid))