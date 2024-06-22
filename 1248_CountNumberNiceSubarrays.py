nums = [1,1,2,1,1]
k = 3

def numberOfSubarrays(nums: list[int], k: int) -> int:
    nums2 = [i%2 for i in nums]
    result = 0
    for taille in range(k, len(nums2)+1):
        i = 0
        while i+taille <= len(nums2):
            # print(nums2[i:i+taille])
            if sum(nums2[i:i+taille]) == k:
                result += 1
            i += 1
    
    return result
        


print(numberOfSubarrays(nums, k))