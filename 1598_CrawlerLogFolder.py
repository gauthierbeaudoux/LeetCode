logs = ["d1/","d2/","../","d21/","./"]

def minOperations(logs: list[str]) -> int:
    compteur = 0
    for i in logs:
        if i == "../":
            if compteur > 0:
                compteur -= 1
        elif i == "./":
            pass
        else:
            compteur += 1
    return compteur


print(minOperations(logs))