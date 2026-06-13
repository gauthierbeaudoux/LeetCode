

def mapWordWeights(words: list[str], weights: list[int]) -> str:
    # print(ord('a'))
    # print(chr(97))
    
    result = ""

    for word in words:
        res = 0
        for lettre in word:
            res += weights[ord(lettre) - 97]
            
        result += chr(ord("z") - res % 26)
        
    return result
            




words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

print(mapWordWeights(words, weights))