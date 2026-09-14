

def isRectangleOverlap(rec1: list[int], rec2: list[int]) -> bool:
    x1 = rec1[0]
    y1 = rec1[1]
    x2 = rec1[2]
    y2 = rec1[3]
    
    x12 = rec2[0]
    y12 = rec2[1]
    x22 = rec2[2]
    y22 = rec2[3]
    
    if x12 >= x2 or y12 >= y2 or x1 >= x22 or y1 >= y22:
        return False
    
    return True
    

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(isRectangleOverlap(rec1, rec2))