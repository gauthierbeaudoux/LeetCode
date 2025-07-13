nums1 = [1,2,2,1]
nums2 = [2,2]


def main(nums1, nums2):
    nums1.sort()
    nums2.sort()
    result = []
    prec = -1
    for nb in nums1:
        l = prec+1
        r = len(nums2)-1
        while r >= l:
            m = (l+r)//2
            if nums2[m] == nb:
                while m > 0 and m-1 >= prec+1 and nums2[m-1] == nb:
                    m -= 1
                result.append(nb)
                prec = m
                break
            elif nums2[m] > nb:
                r = m-1
            else:
                l = m+1
        
    return result
    
print(main(nums1, nums2))