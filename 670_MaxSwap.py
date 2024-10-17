num = 9973

def maximumSwap(num: int) -> int:
    str_num = str(num)
    i = 0
    while i < (len(str_num)-1):
        maxi = max(str_num[i+1:])
        # print(maxi)
        if str_num[i] < maxi:
            inter = str_num[i]
            str_num = str_num[:i] + maxi + str_num[i+1:]
            for j in range(len(str_num)-1, -1, -1):
                if str_num[j] == maxi:
                    str_num = str_num[:j] + inter + str_num[j+1:]
                    return int(str_num)
        i += 1
    
    return num

print(maximumSwap(num))