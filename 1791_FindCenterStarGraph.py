edges = [[1,2],[2,3],[4,2]]

def findCenter(edges: list[list[int]]) -> int:
    a,b = edges[0]
    if a in edges[1]:
        return a
    return b


print(findCenter(edges))