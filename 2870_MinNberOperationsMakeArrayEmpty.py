from collections import Counter

nums = [2,3,3,2,2,4,2,3,4]

def minOperations(nums: list[int]) -> int:
    occurences = Counter(nums)
    nb_actions = 0
    for i in occurences.values():
        test = True
        while test:
            if i % 3 == 0:
                nb_actions += i//3
                test = False
            elif i >= 5:
                i -= 2
                nb_actions += 1
            elif i % 2 == 0:
                nb_actions += i//2
                test = False
            elif i == 1:
                return -1
            else:
                print("Problème")
                test = False
    return nb_actions
            


print(minOperations(nums))