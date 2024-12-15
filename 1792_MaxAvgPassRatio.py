classes = [[1,2],[3,5],[2,2]]
extraStudents = 2

def maxAverageRatio(classes: list[list[int]], extraStudents: int) -> float:
    result = []
    for i in classes:
        result.append(i[0]/i[1])
    
    # print(result)

    for _ in range(extraStudents):
        indice = 0
        mini = -1
        for i in range(len(classes)):
            calcul = (classes[i][0]+1)/(classes[i][1]+1) - result[i]
            if calcul > mini:
                mini = calcul
                indice = i
            
        classes[indice][0] += 1
        classes[indice][1] += 1
        result[indice] = classes[indice][0]/classes[indice][1]
        # print(classes)
        # print(result)
    
    return round(sum(result)/len(result), 5)
        


print(maxAverageRatio(classes, extraStudents))