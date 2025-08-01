numsRows = 3

def generate(numRows: int) -> list[list[int]]:
    result = [[1]]
    for i in range(2, numRows+1):
        inter = []
        for j in range(i):
            if j == 0 or j == i-1:
                inter.append(1)
            else:
                inter.append(result[i-2][j-1]+result[i-2][j])
        result.append(inter)
    
    return result

print(generate(numsRows))