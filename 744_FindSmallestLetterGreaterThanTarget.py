letters = ["c","f","j"]
target = "j"


def nextGreatestLetter(letters: list[str], target: str) -> str:
    l = 0
    r = len(letters)-1
    while r >= l:
        m = (r+l)//2
        # print(f"{l = }")
        # print(f"{r = }")
        # print(f"{m = }")
        if letters[m] == target:
            while m < len(letters) and letters[m] == target:
                m += 1
            if m == len(letters):
                return letters[0]
            return letters[m]
        elif letters[m] > target:
            r = m-1
        else:
            l = m+1
    if l >= len(letters):
        return letters[0]
    return letters[l]
        

print(nextGreatestLetter(letters, target))