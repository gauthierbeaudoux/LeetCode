source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]

def minimumCost(source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
    memoire = [[-1 for i in range(26)] for _ in range(26)]
    def cout_min(entree, sortie, memoire):
        if memoire[ord(entree)-97][ord(sortie)-97] > -1:
            return memoire[ord(entree)-97][ord(sortie)-97]
        min_cout = -1
        for i in range(len(original)):
            if original[i] == entree:
                if changed[i] == sortie:
                    cout = cost[i]
                else:
                    cout = cost[i] + cout_min(changed[i], sortie, memoire)

                if min_cout == -1 or cout < min_cout:
                    min_cout = cout
        
        memoire[ord(entree)-97][ord(sortie)-97] = min_cout
        return min_cout
            
    result = 0    
    for i in range(len(source)):
        if source[i] != target[i]:
            cout_inter = cout_min(source[i], target[i], memoire)
            if cout_inter == -1:
                return -1
            result += cout_inter
    
    
    return result

print(minimumCost(source, target, original, changed, cost))