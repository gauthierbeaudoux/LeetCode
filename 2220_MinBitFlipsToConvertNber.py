start = 10
goal = 7

def minBitFlips(start: int, goal: int) -> int:
    bin_start = "{0:b}".format(start)
    bin_goal = "{0:b}".format(goal)
    result = 0
    m = len(bin_start)
    n = len(bin_goal)
    # print(f"{bin_start = }")
    # print(f"{bin_goal = }")
    for i in range(max(m,n)):
        # print(bin_start[-1-i])
        if i >= m:
            if bin_goal[-1-i] == "1":
                result += 1
        elif i >= n:
            if bin_start[-1-i] == "1":
                result += 1
        elif bin_start[-1-i] != bin_goal[-1-i]:
            result += 1
            
        # print(f"{result = }")
        
    return result


print(minBitFlips(start, goal))