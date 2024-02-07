from collections import Counter

s = "tree"

def frequencySort(s: str) -> str:
    occ_s = Counter(s)
    sorted_dic = dict(sorted(occ_s.items(), key=lambda x: -x[1]))
    return ''.join([i*j for i,j in sorted_dic.items()])

print(frequencySort(s))