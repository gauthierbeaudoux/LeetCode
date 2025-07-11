citations = [1,2]

def main(citations):
    result = 0
    l = 0
    r = len(citations)-1
    while r >= l:
        m = (l+r)//2
        if citations[m] == (len(citations)-m):
            return citations[m]
        elif citations[m] > (len(citations)-m):
            r = m-1
            result = max(len(citations)-m, result)
        else:
            l = m+1
            result = max(result, citations[m])
    return result
    
print(main(citations))