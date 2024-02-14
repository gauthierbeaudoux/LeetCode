nums = [3,1,-2,-5,2,-4]

def rearrangeArray(nums: list[int]) -> list[int]:
    nb_positif = []
    nb_negatif = []
    for x in nums:
        if x > 0:
            nb_positif.append(x)
        else:
            nb_negatif.append(x)

    result = []
    for i in range(len(nb_positif)):
        result.append(nb_positif[i])
        result.append(nb_negatif[i])
    return result

print(rearrangeArray(nums))