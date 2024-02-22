n = 2
trust = [[1,2]]

def findJudge(n: int, trust: list[list[int]]) -> int:
    liste_personne = []
    nb_trust = {}
    for i in range(1,n+1):
        liste_personne.append(i)
        nb_trust[i] = 0
    
    for i in trust:
        if i[0] in liste_personne:
            liste_personne.remove(i[0])
        nb_trust[i[1]] += 1
    
    if len(liste_personne) != 1: return -1
    if nb_trust[liste_personne[0]] == n-1: return liste_personne[0]
    return -1

print(findJudge(n, trust))