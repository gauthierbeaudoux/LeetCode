nums = [0,3,2,1,3,2]

def getSneakyNumbers(nums: list[int]) -> list[int]:
    dico = dict()
    result = []
    for i in nums:
        dico[i] = 1 + dico.get(i,0)
        if dico[i] == 2:
            result.append(i)
            if len(result) == 2:
                return result


print(getSneakyNumbers(nums))