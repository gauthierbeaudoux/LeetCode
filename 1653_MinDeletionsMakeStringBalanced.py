s = "bbaaaaabb"


def minimumDeletions(s: str) -> int:
    
    def valide(liste_a, liste_b):
        if not (liste_a and liste_b) or max(liste_a) < min(liste_b):
            return True
        return False
        
    def exec(pos_a, pos_b, cout):
        if valide(pos_a, pos_b):
            return cout
        else:
            cout_a = exec(pos_a[:-1], pos_b, cout+1)
            cout_b = exec(pos_a, pos_b[1:], cout+1)
            return min(cout_a, cout_b)
        
    pos_b = []
    pos_a = []
    for i in range(len(s)):
        if s[i] == 'a':
            pos_a.append(i)
        else:
            pos_b.append(i)
            
    print(pos_a)
    print(pos_b)
    
    return exec(pos_a, pos_b, 0)
            


print(minimumDeletions(s))