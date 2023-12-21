points = [[8,7],[9,9],[7,4],[9,7]]

def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    def premier_element(L):
        return L[0]

    test = sorted(points, key=premier_element)

    result = 0
    for i in range(len(test)-1):
        if test[i+1][0] - test[i][0] > result:
            result = test[i+1][0] - test[i][0]
    return result

print(maxWidthOfVerticalArea(points))