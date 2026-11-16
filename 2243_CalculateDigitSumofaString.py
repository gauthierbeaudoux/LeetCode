

def digitSum(s: str, k: int) -> str:
    while len(s) > k:
        n = len(s) // k
        if len(s) % k > 0:
            n += 1
        
        new_s = ""
        for j in range(n):
            result = 0
            for i in range(k):
                if i + j*k >= len(s):
                    break
                result += int(s[i+j*k])
                
            new_s += str(result)
            # print(new_s)
            
        s = new_s

    return s


        


s = "11111222223"
k = 3
print(digitSum(s, k))