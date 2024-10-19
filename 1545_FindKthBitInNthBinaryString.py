n = 3
k = 1

def findKthBit(n: int, k: int) -> str:
    s = "0"
    for i in range(n):
        inv_s = s.replace("0", "k")
        inv_s = inv_s.replace("1", "0")
        inv_s = inv_s.replace("k", "1")
        s = s + "1" + inv_s[::-1]
        # print(f"{i = }")
        # print(s)
    
    return s[k-1]

print(findKthBit(n, k))