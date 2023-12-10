matrix = [[1,2,3],[4,5,6],[7,8,9]]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    result = []
    for j in range(len(matrix[0])):
        L = []
        for i in range(len(matrix)):
            L.append(matrix[i][j])
        result.append(L)
    return result

print(transpose(matrix))