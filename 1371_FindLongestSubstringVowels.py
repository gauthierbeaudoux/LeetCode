from collections import Counter

s = "eleetminicoworoep"

def findTheLongestSubstring(s: str) -> int:
    def is_good(occ_lettres):
        voyelle = "aeiou"
        for lettre in voyelle:
            if lettre % 2 != 0:
                return False
            
        return True
        
    count_s = Counter(s)
    if is_good(count_s):
        return True

    

print(findTheLongestSubstring(s))