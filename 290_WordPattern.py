

def wordPattern(pattern: str, s: str) -> bool:
    list_s = s.split(" ")
    
    if len(list_s) != len(pattern):
        return False

    memo = dict()
    for i, lettre in enumerate(pattern):
        if lettre in memo:
            if memo[lettre] != list_s[i]:
                return False
        elif list_s[i] in memo.values() and lettre not in memo:
            return False
        else:
            memo[lettre] = list_s[i]
        
    return True
        

pattern = "abba"
s = "dog dog dog dog"
print(wordPattern(pattern, s))