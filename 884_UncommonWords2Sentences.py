from collections import Counter

s1 = "this apple is sweet"
s2 = "this apple is sour"

def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    sA = s1.split(" ")
    sB = s2.split(" ")
    dico = Counter(sA+sB)
    result = []
    for mot, valeur in dico.items():
        if valeur == 1:
            result.append(mot)
    return result
    

print(uncommonFromSentences(s1, s2))