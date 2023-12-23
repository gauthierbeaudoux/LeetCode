path = "NESWW"

def isPathCrossing(path: str) -> bool:
    x = 0
    y = 0
    stockage = {0: [0]}
    for i in path:
        if i == "N":
            y += 1
        elif i == "S":
            y -= 1
        elif i == "E":
            x += 1
        elif i == "W":
            x -= 1
        if x in stockage:
            if y in stockage[x]:
                return True
            stockage[x].append(y)
        else:
            stockage[x] = [y]
    return False


print(isPathCrossing(path))