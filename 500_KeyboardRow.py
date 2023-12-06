words = ["Hello","Alaska","Dad","Peace"]

words = ["Az"]

def findWords(words: list[str]) -> list[str]:
    result = []
    for j in words:
        a = False
        b = False
        c = False
        for i in j:
            lower_i = i.lower()
            if lower_i in "qwertyuiop":
                if b == False and c == False:
                    a = True
                else:
                    break
            elif lower_i in "asdfghjkl":
                if a == False and c == False:
                    b = True
                else:
                    break
            elif lower_i in "zxcvbnm":
                if a == False and b == False:
                    c = True
                else:
                    break
        else:
            result.append(j)
    return result



print(findWords(words))