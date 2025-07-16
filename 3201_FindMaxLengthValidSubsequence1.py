from collections import Counter

nums = [1,2,3,4]

def main(nums):
    num_pair = [i%2 for i in nums]
    # print(num_pair)
    occ = Counter(num_pair)
    r0 = occ[0]
    r1 = occ[1]
    r_alt = 0
    
    for i in range(len(num_pair)-1):
        if (num_pair[i]+num_pair[i+1]) == 1:
            if r_alt == 0:
                r_alt = 2
            else:
                r_alt += 1
        
    return max(r0, r1, r_alt)
    
print(main(nums))