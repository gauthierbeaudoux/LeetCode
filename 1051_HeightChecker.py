heights = [1,1,4,2,1,3]

def heightChecker(heights: list[int]) -> int:
    trie = sorted(heights)
    result = 0
    for i in range(len(trie)):
        if trie[i] != heights[i]:
            result += 1
    return result

print(heightChecker(heights))