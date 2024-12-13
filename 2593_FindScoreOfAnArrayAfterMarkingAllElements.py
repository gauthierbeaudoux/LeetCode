from collections import Counter

nums = [2,1,3,4,5,2]

def findScore(nums: list[int]) -> int:
    score = 0
    position = [i for i in range(len(nums))]
    while len(position) > 0:
        mini = min(nums)
        pos = nums.index(mini)
        score += mini
        if pos in position:
            position.remove(pos)
        if pos-1 in position:
            position.remove(pos-1)
        if pos+1 in position:
            position.remove(pos+1)
    
    return score
            

    
    

print(findScore(nums))