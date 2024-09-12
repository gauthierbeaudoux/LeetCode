allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

def countConsistentStrings(allowed: str, words: list[str]) -> int:
    result = 0
    for mot in words:
        for lettre in mot:
            if lettre not in allowed:
                break
        else:
            result += 1
    
    return result
                


print(countConsistentStrings(allowed, words))