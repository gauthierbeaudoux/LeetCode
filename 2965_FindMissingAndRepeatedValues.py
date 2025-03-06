grid = [[1,3],[2,2]]

def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
    set_tot = set()
    result = 0
    n = len(grid)
    for i in grid:
        for j in i:
            set_tot.add(j)
            result += j
            
    # print(set_tot)
    somme = n**2*(n**2+1)//2
    # print(somme)
    # print(sum(set_tot))
    chiffre_manquant = somme-sum(set_tot)
    chiffre_double = result-somme+chiffre_manquant
    return [chiffre_double, chiffre_manquant]
    
    

print(findMissingAndRepeatedValues(grid))