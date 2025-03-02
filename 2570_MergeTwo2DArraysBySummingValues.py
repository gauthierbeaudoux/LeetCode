nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]

def mergeArrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    dico = dict()
    for i in nums1:
        dico[i[0]] = i[1]
    
    for i in nums2:
        dico[i[0]] = dico.get(i[0], 0) + i[1]

    dico = dict(sorted(dico.items()))
    
    result = []
    for i,j in dico.items():
        result.append([i, j])

    return result

print(mergeArrays(nums1, nums2))