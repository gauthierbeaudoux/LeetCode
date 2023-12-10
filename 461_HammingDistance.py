x = 4
y = 14

def hammingDistance(x: int, y: int) -> int:
    bin_x = str(bin(x))[2:]
    bin_y = str(bin(y))[2:]
    max_bin = len(bin_x) if x>y else len(bin_y)
    result = 0
    # print(bin_x)
    # print(bin_y)
    for i in range(max_bin):
        if i > len(bin_x)-1:
            if bin_y[-1-i] != '0':
                result += 1
        elif i > len(bin_y)-1:
            if bin_x[-1-i] != '0':
                result += 1
        else:
            if bin_x[-1-i] != bin_y[-1-i]:
                result += 1
    return result
            

print(hammingDistance(x,y))