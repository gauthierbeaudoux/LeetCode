import numpy as np

def shiftGrid(grid: list[list[int]], k: int) -> list[list[int]]:
    liste = []
    m = len(grid)
    n2 = len(grid[0])
    
    for i in range(m):
        liste = liste + grid[i]
        
    # print(liste)
    
    n = len(liste)
    
    result = [-1]*n
    
    for i, val in enumerate(liste):
        result[(i+k) % n] = val
        
    print(result)
    
    result2 = []
    for i in range(m):
        result2.append(result[n2*i:n2*i+n2])
        
    return result2


grid = [[1],[2],[3],[4],[7],[6],[5]]
k = 23
print(shiftGrid(grid, k))