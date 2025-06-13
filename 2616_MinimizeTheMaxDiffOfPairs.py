nums = [3,4,2,3,2,1,2]
p = 3


def minimizeMax(nums: list[int], p: int) -> int:
    if p == 0:
        return 0
    nums.sort()
    
    dist_min = 0
    dist_max = nums[-1]-nums[0]
    if dist_min == dist_max:
        return 0
    
    def is_possible(seuil, nb_pairs):
        compteur = 0
        i = 0
        while i < len(nums)-1:
            if (nums[i+1] - nums[i]) <= seuil:
                compteur += 1
                i += 1
            if compteur == nb_pairs:
                return True
            i += 1
        return False
                
    
    while dist_min < dist_max:
        m = (dist_min+dist_max)//2
        if is_possible(m, p):
            dist_max = m
        else:
            dist_min = m
        if (dist_min+dist_max)//2 == m:
            return dist_max
    


print(minimizeMax(nums, p))