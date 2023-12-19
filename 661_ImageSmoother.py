from math import floor

img = [[1,1,1],[1,0,1],[1,1,1]]
img = [[100,200,100],[200,50,200],[100,200,100]]

def imageSmoother(img: list[list[int]]) -> list[list[int]]:
    nb_ligne = len(img)
    nb_col = len(img[0])
    result = []
    for i in range(nb_ligne):
        L = []
        for j in range(nb_col):
            somme = img[i][j]
            n = 1
            if i+1 < nb_ligne:
                somme += img[i+1][j]
                n += 1
            if i-1 >= 0:
                somme += img[i-1][j]
                n += 1
            if j+1 < nb_col:
                somme += img[i][j+1]
                n += 1
            if j-1 >= 0:
                somme += img[i][j-1]
                n += 1
            if i+1 < nb_ligne and j+1 < nb_col:
                somme += img[i+1][j+1]
                n += 1
            if i-1 >= 0 and j+1 < nb_col:
                somme += img[i-1][j+1]
                n += 1
            if i+1 < nb_ligne and j-1 >= 0:
                somme += img[i+1][j-1]
                n += 1
            if i-1 >= 0 and j-1 >= 0:
                somme += img[i-1][j-1]
                n += 1
            L.append(floor(somme/n))
        result.append(L)
    return result

print(imageSmoother(img))