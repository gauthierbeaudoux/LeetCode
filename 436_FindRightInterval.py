intervals = [[3,4],[2,3],[1,2]]

def main(intervals):
    dico = dict()
    for i in range(len(intervals)):
        dico[intervals[i][0]] = i
        
    sorted_arr = sorted([inter[0] for inter in intervals])
    # print(sorted_arr)
    liste_fin = [inter[1] for inter in intervals]
    
    result = []
    for i in liste_fin:
        l = 0
        r = len(sorted_arr)
        val = -1
        while r > l:
            m = (l+r)//2
            if sorted_arr[m] < i:
                l = m+1
            else:
                r = m
                val = dico[sorted_arr[r]]
        result.append(val)
    
    return result
    
    
    
print(main(intervals))