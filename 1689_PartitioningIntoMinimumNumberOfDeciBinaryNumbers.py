

def minPartitions(n: str) -> int:
    maxi = -1
    for i in n:
        if int(i) > maxi:
            maxi = int(i)
    
    return maxi


n = "32"
print(minPartitions(n))