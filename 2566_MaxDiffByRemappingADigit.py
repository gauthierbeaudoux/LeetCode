num = 90

def minMaxDifference(num: int) -> int:
    string = str(num)
    
    i = 0
    while i < len(string) and string[i] == "9":
        i += 1
    
    if i < len(string):
        maxi = string.replace(string[i], "9")
    else:
        maxi = string
    mini = string.replace(string[0], "0")
    
    # print(maxi)
    # print(mini)
    
    return int(maxi) - int(mini)

print(minMaxDifference(num))