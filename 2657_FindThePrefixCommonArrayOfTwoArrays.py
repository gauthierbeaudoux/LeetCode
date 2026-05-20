from collections import defaultdict

def findThePrefixCommonArray(A: list[int], B: list[int]) -> list[int]:
    result = []
    memo = defaultdict(int)
    
    # for i in range(len(A)):
    #     nbr = 0
    #     for j in A[:i+1]:
    #         if j in B[:i+1]:
    #            nbr += 1
    #     result.append(nbr)
    
    # return result 


    curr = 0
    for i in range(len(A)):
        print(memo)
        
        curr += memo[A[i]]
        memo[A[i]] += 1
        
        curr += memo[B[i]]
        memo[B[i]] += 1
    
        result.append(curr)
        
    return result



A = [1,3,2,4]
B = [3,1,2,4]
print(findThePrefixCommonArray(A, B))