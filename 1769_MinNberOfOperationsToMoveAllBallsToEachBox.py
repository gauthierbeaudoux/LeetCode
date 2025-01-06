boxes = "110"

def minOperations(boxes: str) -> list[int]:
    int_boxes = [int(i) for i in boxes]
    indices = [i for i in range(len(boxes))]
    result = []
    
    for i in range(len(boxes)):
        somme = 0
        for j in range(i+1, len(boxes)):
            somme += int_boxes[j]*indices[j]
            indices[j] -= 1
        for j in range(i):
            somme += int_boxes[j]*indices[j]
            indices[j] += 1
        indices[i] += 1
            
        result.append(somme)
        
    
    return result


print(minOperations(boxes))