skill = [1,5,2,4]
mana = [5,1,4,2]


def minTime(skill: list[int], mana: list[int]) -> int:
    import numpy as np
    precedent = (mana[0]*np.array(skill)).cumsum()
    
    for i in range(1, len(mana)):
        actuel = (mana[i]*np.array(skill)).cumsum()
        maxi = precedent[0]
        for j in range(1, len(actuel)):
            val = precedent[j] - actuel[j-1]
            maxi = max(maxi, val)
        precedent = maxi + actuel
    
    return int(precedent[-1])


print(minTime(skill, mana))