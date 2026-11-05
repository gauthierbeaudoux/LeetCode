

def findTheDistanceValue(arr1: list[int], arr2: list[int], d: int) -> int:
    result = 0
    
    for i in arr1:
        for j in arr2:
            if abs(i-j) <= d:
                break
        else:
            result += 1
    
    return result
                


arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
print(findTheDistanceValue(arr1, arr2, d))