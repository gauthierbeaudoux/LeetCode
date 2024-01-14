from collections import Counter

word1 = "cabbba"
word2 = "abbccc"

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    list1 = Counter(word1)
    list2 = Counter(word2)
    if sorted(list1.keys())==sorted(list2.keys()) and sorted(list1.values())==sorted(list2.values()):
        return True
    return False


print(closeStrings(word1,word2))