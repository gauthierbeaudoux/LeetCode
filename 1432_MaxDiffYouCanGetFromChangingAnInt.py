num = 1101057

def maxDiff(num: int) -> int:
    
    i = 0
    str_num = str(num)
    if str_num[0] == "1":
        while i < len(str_num) and (str_num[i] == "1" or str_num[i] == "0"):
            i += 1
        if i < len(str_num):
            mini = str_num.replace(str_num[i], "0")
        else:
            mini = str_num
    else:
        mini = str_num.replace(str_num[0], "1")
    
        
    i = 0
    while i < len(str_num) and str_num[i] == "9":
        i += 1
    if i < len(str_num):
        maxi = str_num.replace(str_num[i], "9")
    else:
        maxi = str_num
        
    # print(maxi)
    # print(mini)
        
    return int(maxi) - int(mini)
        
    
    


print(maxDiff(num))