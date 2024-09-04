commands = [4,-1,4,-2,4]
obstacles = [[2,4]]

def robotSim(commands: list[int], obstacles: list[list[int]]) -> int:
    x = 0
    y = 0
    L = [[0,1], [1,0], [0,-1], [-1,0]]
    i = 0
    result = 0
    for comm in commands:
        if comm == -1:
            i += 1
        elif comm == -2:
            i -= 1
        else:
            for _ in range(comm):
                new_x = x + L[i][0]
                new_y = y + L[i][1]
                
                if [new_x, new_y] in obstacles:
                    break
                x = new_x
                y = new_y
              
        result = max(result, x**2+y**2)      
        i = i%4
        
        # print(f"{x = }")
        # print(f"{y = }")
        
    return result

print(robotSim(commands, obstacles))