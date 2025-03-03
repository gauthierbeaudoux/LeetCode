nums = [9,12,5,10,14,3,10]
pivot = 10


def pivotArray(nums: list[int], pivot: int) -> list[int]:
    indice_pivot = nums.index(10)
    nb_inser = 0
    nb_pivot = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0.5:
            i += 1
        else:
            if i < indice_pivot:
                if nums[i] > pivot:
                    val = nums[i]
                    nums[i] == 0.5
                    nums.insert(indice_pivot+nb_inser+1, val)
                    nb_inser += 1
                elif nums[i] == pivot:
                    val = nums[i]
                    nums[i] == 0.5
                    nums.insert(indice_pivot, val)
                    nb_pivot += 1
                else:
                    i += 1
            elif i > indice_pivot+nb_pivot:
                if nums[i] < pivot:
                    val = nums[i]
                    nums[i] == 0.5
                    nums.insert(indice_pivot, val)
                elif nums[i] == pivot:
                    val = nums[i]
                    nums[i] == 0.5
                    nums.insert(indice_pivot+1, val)
                    nb_pivot += 1
                else:
                    i += 1
            else:
                i += 1
            
        print(nums)
    
    return nums
            
                


print(pivotArray(nums, pivot))