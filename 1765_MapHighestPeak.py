isWater = [[0,1],[0,0]]

def highestPeak(isWater: list[list[int]]) -> list[list[int]]:
    
    def is_not_full(L):
        for i in range(nb_lignes):
            if min(L[i]) == -1:
                return True
        return False
        
    
    nb_lignes = len(isWater)
    nb_col = len(isWater[0])
    L = [[-1 for _ in range(nb_col)] for _ in range(nb_lignes)]
    # print(L)
    
    for i in range(nb_lignes):
        for j in range(nb_col):
            if isWater[i][j] == 1:
                L[i][j] = 0
    
    hauteur = 1
    while is_not_full(L):
        for i in range(nb_lignes):
            for j in range(nb_col):
                if L[i][j] == hauteur-1:
                    if i > 0 and L[i-1][j] == -1:
                        L[i-1][j] = hauteur
                    if i < nb_lignes-1 and L[i+1][j] == -1:
                        L[i+1][j] = hauteur
                    if j > 0 and L[i][j-1] == -1:
                        L[i][j-1] = hauteur
                    if j < nb_col-1 and L[i][j+1] == -1:
                        L[i][j+1] = hauteur
        hauteur += 1

    return L

    
print(highestPeak(isWater))