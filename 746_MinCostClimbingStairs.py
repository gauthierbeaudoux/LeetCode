

def minCostClimbingStairs(cost: list[int]) -> int:
    prev2 = cost[0]
    prev1 = cost[1]
    
    for i in range(2, len(cost)):
        prev2, prev1 = prev1, cost[i]+min(prev1, prev2)
    
    return min(prev1, prev2)
    
    
    

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))