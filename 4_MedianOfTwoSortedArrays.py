nums1 = [1,2]
nums2 = [3,4]

def main(nums1, nums2):
    num = nums1 + nums2
    num.sort()
    n = len(num)
    if n % 2 == 1:
        return num[n//2]
    else:
        return (num[n//2-1] + num[n//2])/2
    
print(main(nums1, nums2))