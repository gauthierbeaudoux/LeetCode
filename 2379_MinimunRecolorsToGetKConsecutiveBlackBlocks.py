blocks = "WBBWWBBWBW"
k = 7

def minimumRecolors(blocks: str, k: int) -> int:
    i = 0
    extract = blocks[:k]
    count = extract.count('B')
    maxi = count
    while (i+k) < len(blocks):
        if blocks[i] == 'B':
            count -= 1
        if blocks[k+i] == 'B':
            count += 1
        
        maxi = max(maxi, count)
        i += 1
    
    return k-maxi
        

print(minimumRecolors(blocks, k))