numsRows = 3

def generate(numRows: int) -> list[list[int]]:
    result = [[1]]
    if numRows == 1:
        return result
    for i in range(1,numRows):
        list_temp = [1]
        for j in range(i-1):
            list_temp.append(result[i-1][j]+result[i-1][j+1])
        list_temp.append(1)
        result.append(list_temp)
    return result

print(generate(numsRows))