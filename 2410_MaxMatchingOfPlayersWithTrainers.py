players = [4,7,9]
trainers = [8,2,5,8]

def main(players, trainers):
    players.sort()
    trainers.sort()
    
    result = 0
    prec = -1
    for val in players:
        l = prec+1
        prec = -1
        r = len(trainers)-1
        while r >= l:
            m = (l+r)//2
            if trainers[m] >= val:
                r = m-1
                prec = m
            else:
                l = m+1
        if prec == -1:
            break
        else:
            result += 1
                
    return result
    
print(main(players, trainers))