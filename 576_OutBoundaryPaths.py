m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0


def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    def moving(m,n,maxMove, startRow, startColumn, L):
        L[startRow][startColumn] = False
        result = 0
        if startRow == 0:
            result += 1
        if startRow == m-1:
            result += 1
        if startColumn == 0:
            result += 1
        if startColumn == n-1:
            result += 1

        if maxMove == 1:
            return result

        if startRow + 1 < m and L[startRow+1][startColumn]:
            result += moving(m, n, maxMove - 1, startRow + 1, startColumn, L)
        if startRow - 1 >= 0 and L[startRow-1][startColumn]:
            result += moving(m, n, maxMove - 1, startRow - 1, startColumn, L)
        if startColumn + 1 < n and L[startRow][startColumn+1]:
            result += moving(m, n, maxMove - 1, startRow, startColumn + 1, L)
        if startColumn - 1  >= 0 and L[startRow][startColumn-1]:
            result += moving(m, n, maxMove - 1, startRow, startColumn - 1, L)
        
        return result

    L = [[True]*n for i in range(m)]
    return moving(m,n,maxMove, startRow, startColumn, L)

print(findPaths(m,n,maxMove, startRow, startColumn))                