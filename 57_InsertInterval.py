intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result = []
    liste_en_cours = False
    inter_ajoute = False
    debut = newInterval[0]
    fin = newInterval[1]
    
    if intervals == []:
        return [newInterval]
    
    if intervals[-1][1] < debut:
        return intervals + [newInterval]
    
    for inter in intervals:
        if inter_ajoute:
            result.append(inter)
        elif liste_en_cours:
            if liste_inter[1] < inter[0]:
                result.append(liste_inter)
                result.append(inter)
                liste_en_cours = False
                inter_ajoute = True
            elif liste_inter[1] > inter[1]:
                continue
            elif liste_inter[1] <= inter[1]:
                result.append([liste_inter[0], inter[1]])
                liste_en_cours = False
                inter_ajoute = True
            else:
                print('Erreur')
        elif fin < inter[0]:
            result.append(newInterval)
            result.append(inter)
            inter_ajoute = True
        elif debut > inter[1]:
            result.append(inter)
        elif fin >= inter[1] or debut <= inter[0]:
            liste_inter = [min(inter[0], debut), max(fin, inter[1])]
            liste_en_cours = True
        elif debut >= inter[0] and fin <= inter[1]:
            result.append(inter)
            inter_ajoute = True
        else:
            result.append(inter)
    
    if liste_en_cours:
        result.append(liste_inter)
    
    return result
                
            

print(insert(intervals, newInterval))