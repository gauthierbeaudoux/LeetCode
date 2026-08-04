from collections import defaultdict

def findMissingElements(nums: list[int]) -> list[int]:
    mini = nums[0]
    maxi = nums[0]

    dico = defaultdict(int)
    
    for i in nums:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
            
        dico[i] = 1
        
    result = []
    for i in range(mini+1, maxi):
        if dico[i] == 0:
            result.append(i)
            
    return result

    


nums = [1,4,2,5]
print(findMissingElements(nums))