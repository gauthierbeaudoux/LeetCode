nums = [1,2,3,4,3,2,5]
k = 3

def resultsArray(nums: list[int], k: int) -> list[int]:
    def fonc(liste):
        for i in range(len(liste)-1):
            if liste[i]+1 != liste[i+1]:
                return -1
        return max(liste)
            
    result = []
    n = len(nums)
    i = 0
    while (i+k) <= n:
        result.append(fonc(nums[i:i+k]))
        i += 1
    
    return result
        
print(resultsArray(nums, k))