matrix = [[2,1,3],[6,5,4],[7,8,9]]
# matrix = [[-19,57],[-40,-5]]


def minFallingPathSum(matrix: list[list[int]]) -> int:
    global list_memoire
    n = len(matrix)
    list_memoire = [['s']*n]*n
    def court_chemin(matrix, i, j):
        if i == len(matrix)-1:
            return matrix[i][j]
        if list_memoire[i+1][j] == 's':
            min_bas = court_chemin(matrix, i+1, j)
            list_memoire[i+1][j] = min_bas
        else:
            min_bas = list_memoire[i+1][j]

        min_gauche = 100*len(matrix)+1
        min_droite = 100*len(matrix)+1

        if j-1 > 0 or (j-1 == 0 and matrix[i+1][j-1] < matrix[i+1][j]):
            if list_memoire[i+1][j-1] == 's':
                min_gauche = court_chemin(matrix, i+1, j-1)
                list_memoire[i+1][j-1] = min_gauche
            else:
                min_gauche = list_memoire[i+1][j-1]

        if j+1 < len(matrix)-1 or (j+1 == len(matrix)-1 and matrix[i+1][j+1] < matrix[i+1][j]):
            if list_memoire[i+1][j+1] == 's':
                min_droite = court_chemin(matrix, i+1, j+1)
                list_memoire[i+1][j+1] = min_droite
            else:
                min_droite = list_memoire[i+1][j+1]
            
        valeur = min(min_bas, min_gauche, min_droite) + matrix[i][j]
        return valeur
    
    minimum = 100*len(matrix)+1
    for j in range(len(matrix)):
        minimum = min(minimum, court_chemin(matrix, 0, j))

    return minimum


print(minFallingPathSum(matrix))