from math import sqrt

area = 122122


def constructRectangle(area: int) -> list[int]:
    L = int(sqrt(area))
    while L <= area:
        if area % L == 0:
            W = area//L
            return [max(L,W), min(L,W)]
        else:
            L -= 1


print(constructRectangle(area))