jobDifficulty = [1,1,1]
d = 3

def minDifficulty(jobDifficulty: list[int], d: int) -> int:
    if len(jobDifficulty) < d:
        return -1
    result = 0
    for i in range(d):
        if i == d-1:
            return result + max(jobDifficulty[i:])
        result += jobDifficulty[i]

print(minDifficulty(jobDifficulty, d))