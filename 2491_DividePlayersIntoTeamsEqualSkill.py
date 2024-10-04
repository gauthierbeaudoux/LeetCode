skill = [3,2,5,1,3,4]

def dividePlayers(skill: list[int]) -> int:
    skill.sort()
    result = skill[0] + skill[-1]
    result2 = skill[0]*skill[-1]
    for i in range(1, len(skill)//2):
        if (skill[i] + skill[-1-i]) != result:
            return -1
        result2 += skill[i]*skill[-1-i]
    
    return result2
    

print(dividePlayers(skill))