s = "mgntdygtxrvxjnwksqhxuxtrv"

def maxLengthBetweenEqualCharacters(s: str) -> int:
    result = -1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pos_lettre = {}
    for i in alphabet:
        pos_lettre[i] = -1
    for position, lettre in enumerate(s):
        if pos_lettre[lettre] == -1:
            pos_lettre[lettre] = position
        else:
            distance = position - pos_lettre[lettre] - 1
            if distance > result:
                result = distance
    return result

    


print(maxLengthBetweenEqualCharacters(s))