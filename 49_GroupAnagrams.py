from collections import Counter, defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    memo = dict()
    res = []
    
    for mot in strs:
        sorted_word = "".join(sorted(mot))
    
        if sorted_word in memo:
            res[memo[sorted_word]].append(mot)
        else:
            res.append([mot])
            memo[sorted_word] = len(res)-1

    return res



strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["abets","bead","remain","betas","abed","baste","airline","leading","beast","dealing","beats","airmen","marine","single","bade","aligned"]
print(groupAnagrams(strs))