matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def main(matrix, target):
    sorted_arr = []
    for i in matrix:
        sorted_arr += i
    
    l = 0
    r = len(sorted_arr)-1
    while r >= l:
        m = (l+r)//2
        if sorted_arr[m] == target:
            return True
        elif sorted_arr[m] > target:
            r = m-1
        else:
            l = m+1
    return False
    
print(main(matrix, target))