nums = [3,2,3]

def majorityElement(nums: list[int]) -> int:
    elements = {}
    n = len(nums)
    for i in nums:
        if i in elements.keys():
            elements[i] += 1
        else:
            elements[i] = 1
        if elements[i] >= n/2: return i
    
print(majorityElement(nums))