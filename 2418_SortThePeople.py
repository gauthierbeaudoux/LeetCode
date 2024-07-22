names = ["Mary","John","Emma"]
heights = [180,165,170]

def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    new_list = [[names[i], heights[i]] for i in range(len(names))]
    new_list.sort(key= lambda x: -x[1])
    return [new_list[i][0] for i in range(len(names))]


print(sortPeople(names, heights))