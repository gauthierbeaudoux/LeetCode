n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

def getAncestors(n: int, edges: list[list[int]]) -> list[list[int]]:
    result = dict()
    for i in range(n):
        result[i] = set()
    
    for node in edges:
        result[node[1]].add(node[0])
    
    # print(result)

    for _ in range(2):
        for i in range(n):
            for value in result[i]:
                result[i] = result[i] | result[value]
    
    # print(result)
    
    result2 = []
    for i in range(n):
        if result[i] == set():
            result2.append([])
        else:
            result2.append(sorted(list(result[i])))
    
    # print(result2)
    return result2
            
    
    
print(getAncestors(n, edgeList))