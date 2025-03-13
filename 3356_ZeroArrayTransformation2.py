import numpy as np

nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]

def minZeroArray(nums: list[int], queries: list[list[int]]) -> int:
    
    np_nums = np.array(nums)
    n = len(nums)
    # print(np.array([0]*0))
    if all(np_nums <= 0):
            return 0
    
    for i, query in enumerate(queries):
        m = query[1] - query[0]
        liste = [0]*query[0] + [query[2]]*(m+1) + [0]*(n-query[1]-1)
        print(liste)
        np_liste = np.array(liste)
        np_nums -= np_liste
        print(np_nums)
        
        if all(np_nums <= 0):
            return i+1
    
    return -1


print(minZeroArray(nums, queries))