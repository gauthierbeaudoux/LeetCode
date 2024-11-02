sentence = "leetcode exercises sound delightful"

def isCircularSentence(sentence: str) -> bool:
    spl = sentence.split()
    if spl[-1][-1] != spl[0][0]:
        return False
    i = 0
    while i+1 < len(spl):
        if spl[i][-1] != spl[i+1][0]:
            return False
        i += 1
    
    return True
        

print(isCircularSentence(sentence))