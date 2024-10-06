sentence1 = "d T d ED uXW L U J n klIe"
sentence2 = "d T d ED uXW L U J klIe"

def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    l1 = sentence1.split()
    l2 = sentence2.split()
    if len(l1) <= len(l2):
        l_court = l1
        l_long = l2
    else:
        l_court = l2
        l_long = l1
    
    
    indices = [i for i in range(len(l_long))] 
    for mot in l_court:
        # print(ind)
        # print(mot)
        if mot not in l_long:
            return False
        # print(f"{indices = }")
        # print(f"{mot = }")
        j = 0
        while j < len(l_long):
            to_remove = l_long.index(mot, j)
            if to_remove in indices:
                indices.remove(l_long.index(mot))
                break
            j += 1
                
    
    i = 0
    while i < (len(indices)-1):
        if (indices[i+1] - indices[i]) > 1:
            return False
        i += 1
        
    return True
        
    

print(areSentencesSimilar(sentence1, sentence2))