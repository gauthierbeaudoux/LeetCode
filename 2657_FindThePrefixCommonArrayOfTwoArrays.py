A = [1,3,2,4]
B = [3,1,2,4]

def findThePrefixCommonArray(A: list[int], B: list[int]) -> list[int]:
    result = []
    
    for i in range(len(A)):
        nbr = 0
        for j in A[:i+1]:
            if j in B[:i+1]:
               nbr += 1
        result.append(nbr)
    
    return result 


print(findThePrefixCommonArray(A, B))