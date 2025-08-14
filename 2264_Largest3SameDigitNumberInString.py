num = "6777133339"

def largestGoodInteger(num: str) -> str:
    result = ""
    for i in range(len(num)-2):
        if num[i] == num[i+1] and num[i+1] == num[i+2]:
            if result == "":
                result = num[i:i+3]
            else:
                result = str(max(int(result), int(num[i:i+3])))
        
    if result == "0":
        return "000"
    return result
        


print(largestGoodInteger(num))