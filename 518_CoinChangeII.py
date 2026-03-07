from collections import defaultdict

def change(amount: int, coins: list[int]) -> int:
    
    memo = defaultdict(int)
    def dfs(i, total):
        if total == 0:
            return 1
        elif total < 0:
            return 0
    
        if i >= len(coins):
            return 0
        
        if (i, total) in memo:
            return memo[(i, total)]
        
        
        # for j in range(i, len(coins)):
        #     if total-coins[j] >= 0:
        #         memo[(i, total)] += dfs(j, total-coins[j])

        memo[(i, total)] = dfs(i, total-coins[i]) + dfs(i+1, total)
            
        return memo[(i, total)]

    return dfs(0, amount)

amount = 5
coins = [1,2,5]
print(change(amount, coins))