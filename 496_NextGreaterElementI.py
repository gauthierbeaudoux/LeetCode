from collections import deque, defaultdict

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = deque()
    result = [-1]*len(nums1)
    
    pos_result = defaultdict(lambda: -1)
    for i, val in enumerate(nums1):
        pos_result[val] = i
    
    for i, val in enumerate(nums2):
        
        while stack and nums2[stack[-1]] < val:
            if pos_result[nums2[stack[-1]]] > -1:
                result[pos_result[nums2[stack[-1]]]] = val
            stack.pop()
        
        if pos_result[val] > -1:
            stack.append(i)
        
    return result
        
    


nums1 = [1,3,5,2,4]
nums2 = [5,4,3,2,1]
print(nextGreaterElement(nums1, nums2))