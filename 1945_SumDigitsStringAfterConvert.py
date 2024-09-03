s = "leetcode"
k = 2

def getLucky(s: str, k: int) -> int:
    result = 0
    for lettre in s:
        print(lettre)
        nbr = ord(lettre)-96
        if nbr >= 10:
            for lettre in str(nbr):
                print(lettre)
                result += int(lettre)
        else:
            print(nbr)
            result += nbr
        
        print(f"{result = }")
        # print(nbr)
        
    for i in range(k-1):
        str_result = str(result)
        result = 0
        for lettre in str_result:
            result += int(lettre)
        
    return result

print(getLucky(s, k))