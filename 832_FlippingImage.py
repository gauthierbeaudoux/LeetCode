image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]


def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
    n = len(image)
    for i in range(n):
        for j in range(n//2):
            image[i][j], image[i][n-j-1] = image[i][n-j-1], image[i][j]
    for i in range(n):
        for j in range(n):
            image[i][j] = abs(image[i][j]-1)
    return image



print(flipAndInvertImage(image))