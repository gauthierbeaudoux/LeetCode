words = ["abc","car","ada","racecar","cool"]

def firstPalindrome(words: list[str]) -> str:
    def is_palindrom(word):
        for i in range(len(word)//2):
            if word[i] != word[-1-i]:
                return False
        return True
    
    for mot in words:
        if is_palindrom(mot):
            return mot
    return ""


print(firstPalindrome(words))