from collections import Counter

nums = [2,3,1,3,2]

def frequencySort(nums: list[int]) -> list[int]:
    occ = Counter(nums)
    trie = dict(sorted(occ.items(), key=lambda x: x[1]*1000 - x[0]))
    print(trie)
    result = []
    for cle, valeur in trie.items():
        result += [cle for _ in range(valeur)]
    
    return result
    


print(frequencySort(nums))