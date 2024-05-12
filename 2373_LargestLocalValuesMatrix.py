grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]

def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    
    def findMax(grid, i, j):
        maxi = 0
        for ik in range(3):
            for jk in range(3):
                current = grid[i-1+ik][j-1+jk]
                if current > maxi:
                    maxi = current
        return maxi
                
    nb_lignes = len(grid)
    nb_col = len(grid[0])
    result = []
    for ligne in range(1, nb_lignes-1):
        current_ligne = []
        for col in range(1, nb_col-1):
            current_ligne.append(findMax(grid, ligne, col))
        result.append(current_ligne)
    
    return result



print(largestLocal(grid))