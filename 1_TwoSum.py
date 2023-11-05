nums = [2,7,11,15]
target = 9


# Brute force

def brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return ([i, j])
    return []

def hash_map(nums, target):
    memoire = {}
    for indice, value in enumerate(nums):
        obj_value = target - value
        if obj_value in memoire:
            return [memoire[obj_value], indice]
        memoire[value] = indice
    return []

print(brute_force(nums, target))
print(hash_map(nums, target))