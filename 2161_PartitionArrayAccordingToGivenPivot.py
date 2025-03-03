nums = [9,12,5,10,14,3,10]
pivot = 10


def pivotArray(nums: list[int], pivot: int) -> list[int]:
    inf = []
    egal = []
    sup = []
    for i in nums:
        if i < pivot:
            inf.append(i)
        elif i > pivot:
            sup.append(i)
        else:
            egal.append(i)
    
    
    return inf + egal + sup
            
    
    
    
            
                


print(pivotArray(nums, pivot))