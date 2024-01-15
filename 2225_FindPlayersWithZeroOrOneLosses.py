from collections import Counter

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

def findWinners(matches: list[list[int]]) -> list[list[int]]:
    vainqueur = set()
    perdant = []
    for i in matches:
        vainqueur.add(i[0])
        perdant.append(i[1])

    for j in perdant: vainqueur.discard(j)
    
    compteur = Counter(perdant)
    to_delete = []
    for i,j in compteur.items():
        if j > 1: to_delete.append(i)
    for i in to_delete:
        del compteur[i]
    
    return sorted(list(vainqueur)), sorted(list(compteur))

print(findWinners(matches))
