
def minimumCost(cost: list[int]) -> int:
    triee = sorted(cost, reverse=True)
    result = 0
    for i, val in enumerate(triee):
        if i % 3 < 2:
            result += val

    return result


cost = [1,2,3]
print(minimumCost(cost))