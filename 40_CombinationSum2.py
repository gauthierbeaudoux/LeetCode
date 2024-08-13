candidates = [10,1,2,7,6,1,5]
target = 8

def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    
    def interne(candidates, target, memoire):
        if target == 0:
            return memoire
            
        if len(candidates) == 0:
            return None
        
        if candidates[0] > target:
            return interne(candidates[1:], target, memoire)
        
        if candidates[0] == target:
            
        
        
        result = set()
    

print(combinationSum2(candidates, target))