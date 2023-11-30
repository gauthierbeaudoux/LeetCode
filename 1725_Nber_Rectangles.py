rectangles = [[5,8],[3,9],[5,12],[16,5]]
rectangles = [[2,3],[3,7],[4,3],[3,7]]

def countGoodRectangles(rectangles: list[list[int]]) -> int:
    max_len = -1
    for i in rectangles:
        taille_carre = min(i)
        if taille_carre > max_len:
            max_len = taille_carre
            total = 1
        elif taille_carre == max_len:
            total += 1
    return total


print(countGoodRectangles(rectangles))