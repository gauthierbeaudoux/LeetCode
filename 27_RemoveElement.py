
nums = [3,2,2,3]
val = 3

def removeElement(list_nums, valeur):
    i = 0
    k = 0
    while i < len(list_nums):
        if list_nums[i] == valeur:
            list_nums.remove(valeur)
            k += 1
        else:
            i += 1
    return i


print(removeElement(nums, val))
print(nums)