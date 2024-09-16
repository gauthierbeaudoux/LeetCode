timePoints = ["00:00","04:00","22:00"]

def findMinDifference(timePoints: list[str]) -> int:
    def distance(i1, i2):
        return min((i1-i2) % 1440, (i2-i1) % 1440)
    
    in_minutes = [int(i[:2])*60 + int(i[3:]) for i in timePoints]
    in_minutes.sort()
    print(in_minutes)
    result = distance(in_minutes[0], in_minutes[-1])
    for i in range(len(in_minutes)-1):
        result = min(result, distance(in_minutes[i], in_minutes[i+1]))
    return result
    


print(findMinDifference(timePoints))