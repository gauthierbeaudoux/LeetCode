from collections import Counter

s = "101"

def minimumSteps(s: str) -> int:
    occ = Counter(s)
    # print(occ)
    # left_counter = 0
    result = 0
    for i in range(occ['1']):
        # print(i)
        if s[-1-i] == '0':
            result += 1
            
    return result
            
            
    

print(minimumSteps(s))