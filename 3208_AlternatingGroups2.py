colors = [0,1,0,1,0]
k = 3

def numberOfAlternatingGroups(colors: list[int], k: int) -> int:
    colors2 = colors + colors
    result = 0
    for i in range(len(colors)):
        for n in range(k-1):
            if colors2[i+n] == colors2[i+1+n]:
                break
        else:
            result += 1
    
    return result


print(numberOfAlternatingGroups(colors, k))