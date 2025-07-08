letters = ["c","f","j"]
target = "j"


def nextGreatestLetter(letters: list[str], target: str) -> str:
    l = 0
    r = len(letters)
    while r > l:
        m = (r+l)//2
        if letters[m] <= target:
            l = m+1
        else:
            r = m
    return letters[l%len(letters)]
        

print(nextGreatestLetter(letters, target))