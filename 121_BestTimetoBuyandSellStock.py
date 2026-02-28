

def maxProfit(prices: list[int]) -> int:
    mini = prices[0]
    res = 0
    
    for i in prices:
        if i < mini:
            mini = i
        
        res = max(res, i-mini)

    return res



prices = [7,1,5,3,6,4]
print(maxProfit(prices))