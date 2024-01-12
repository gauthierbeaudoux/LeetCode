s = "book"

def halvesAreAlike(s: str) -> bool:
    voyelles = 'aeiouAEIOU'
    n = len(s)
    a = s[:n//2]
    b = s[n//2:]
    result_a = 0
    result_b = 0
    for lettre in a:
        if lettre in voyelles: result_a += 1
    for lettre in b:
        if lettre in voyelles: result_b += 1

    return result_a == result_b


print(halvesAreAlike(s))