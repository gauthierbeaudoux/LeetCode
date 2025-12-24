apple = [1,3,2]
capacity = [4,3,1,5,2]

def minimumBoxes(apple: list[int], capacity: list[int]) -> int:
    capacity.sort(reverse=True)
    total = sum(apple)
    result = 0
    for i in capacity:
        total -= i
        result += 1
        if total <= 0:
            return result



print(minimumBoxes(apple, capacity))