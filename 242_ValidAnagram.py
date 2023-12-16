s = "ab"
t = "a"

def isAnagram(s: str, t: str) -> bool:
    # list_s = list(s)
    # list_t = list(t)
    # for i in list_t:
    #     if i in list_s:
    #         list_s.remove(i)
    #     else:
    #         return False
    # if list_s:
    #     return False
    # return True

    return sorted(s) == sorted(t)


print(isAnagram(s,t))