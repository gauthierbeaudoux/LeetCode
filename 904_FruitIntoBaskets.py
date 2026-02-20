from collections import Counter, defaultdict

def totalFruit(fruits: list[int]) -> int:
    result = 0
    memo = defaultdict(int)
    left = 0
    
    for i, valeur in enumerate(fruits):
        memo[valeur] += 1
        
        while len(memo) > 2:
            memo[fruits[left]] -= 1
            if memo[fruits[left]] == 0:
                del memo[fruits[left]]
            left += 1
        
        result = max(result, sum(memo.values()))
        
    return result


fruits = [1,2,3,2,2]
print(totalFruit(fruits))