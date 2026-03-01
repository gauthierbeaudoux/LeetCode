from collections import defaultdict

def coinChange(coins: list[int], amount: int) -> int:
    memo = defaultdict(lambda: float('inf'))
    
    def dfs(target):
        if target == 0:
            return 0
        if target < 0:
            return Exception("target < 0")
        if target in memo:
            return memo[target]
        
        for i in coins:
            if i > target:
                continue
            memo[target] = min(memo[target], dfs(target-i)+1)
        
        return memo[target]
    
    res = dfs(amount)
    if res == float("inf"):
        return -1
    return res


coins = [1,2,5]
amount = 45
print(coinChange(coins, amount))