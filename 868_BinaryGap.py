

def binaryGap(n: int) -> int:
    binary = bin(n)[2:]
    left = 0
    right = 1
    res = 0
    # print(f'{binary = }')
    while right <= len(binary):
        
        while right < len(binary) and binary[right] == "0":
            right += 1
        
        # print(f"{right = }")
        while left < len(binary) and binary[left] == "0":
            left += 1
        # print(f"{left = }")
        
        if right < len(binary) and left < len(binary):
            res = max(res, right-left)
        left = right
        right += 1
        
    return res
    

n = 29
print(binaryGap(n))