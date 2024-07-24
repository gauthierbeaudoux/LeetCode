mapping = [8,2,9,5,3,7,1,0,6,4]
nums = [418,4191,916,948,629641556,574,111171937,28250,42775632,
        6086,85796326,696292542,186,67559,2167,366,854,2441,78176,
        621,4257,2250097,509847,7506,77,50,4135258,4036,59934,59474,
        3646243,9049356,85852,90298188,2448206,30401413,33190382,
        968234660,7973,668786,992777977,77,355766,221,246409664,
        216290476,45,87,836414,40952]

def sortJumbled(mapping: list[int], nums: list[int]) -> list[int]:
    dico = dict()
    doublons = []
    for nombre in nums:
        if nombre in dico.keys():
            doublons.append(nombre)
        valeur = ''
        for chiffre in str(nombre):
            valeur += str(mapping[int(chiffre)])
        dico[nombre] = int(valeur)
    
    # print(dico)
    trie = dict(sorted(dico.items(), key=lambda x: x[1]))
    # print(trie)
    result = []
    liste_triee = list(trie.keys())
    n = len(liste_triee)
    i = 0
    while i < n:
        if liste_triee[i] in doublons:
            result.append(liste_triee[i])
            doublons.remove(liste_triee[i])
            print("OUI")
        else:
            result.append(liste_triee[i])
            i += 1
            
    return result

print(sortJumbled(mapping, nums))