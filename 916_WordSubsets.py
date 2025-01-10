from collections import Counter

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

def wordSubsets(words1: list[str], words2: list[str]) -> list[str]:
    def is_subset(a, b):
        occ_a = Counter(a)
        occ_b = Counter(b)
        for cles in occ_a.keys():
            if cles not in b:
                return False
            if occ_a[cles] > occ_b[cles]:
                return False
        return True
    
    result = []
    
    for mot in words1:
        for mot2 in words2:
            if not is_subset(mot2, mot):
                break
        else:
            result.append(mot)
    
    return result


print(wordSubsets(words1, words2))