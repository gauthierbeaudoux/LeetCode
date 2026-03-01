

def mincostTickets(days: list[int], costs: list[int]) -> int:
    memo = dict()
    def recu(i, jour):
        while i < len(days) and days[i] < jour:
            i += 1
            
        if i == len(days):
            return 0
        
        if i in memo:
            return memo[i]
        
        jour = days[i]
        memo[i] = min(recu(i+1, jour+1)+costs[0],
                   recu(i+1, jour+7)+costs[1],
                   recu(i+1, jour+30)+costs[2])
        return memo[i]

    return recu(0, 1)


days = [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
costs = [3,13,45]
print(mincostTickets(days, costs))