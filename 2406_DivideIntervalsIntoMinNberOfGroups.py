intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

def minGroups(intervals: list[list[int]]) -> int:
    intervals.sort()
    # print(intervals)
    result = 0
    while intervals:
        result += 1
        val = intervals[0]
        del intervals[0]
        j = 0
        while j < len(intervals):
            if val[1] < intervals[j][0]:
                val = intervals[j]
                del intervals[j]
            else:
                j += 1
    
    return result
        
        
print(minGroups(intervals))