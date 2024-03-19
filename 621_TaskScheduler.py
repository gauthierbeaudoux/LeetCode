from collections import Counter

tasks = ["A","A","A","B","B","B"]
n = 2

def leastInterval(tasks: list[str], n: int) -> int:
    result = 0
    occ = Counter(tasks)
    while ....:
        for i in range(n):
            occ[i] -= 1
            result += 1
    
print(leastInterval(tasks,n))