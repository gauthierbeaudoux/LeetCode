nums = [1,2,3,4,2,3,3,5,7]

def minimumOperations(nums: list[int]) -> int:
    def check_distinct(liste):
        L = []
        for i in liste:
            if i in L:
                return True
            L.append(i)
        return False
    
    result = 0
    i = 0
    while i < len(nums) and check_distinct(nums[i:]):
        i += 3
        result += 1
    
    return result


print(minimumOperations(nums))