

def minimumPushes(word: str) -> int:
    diviseur = len(word) // 8
    reste = len(word) % 8
    # print(len(word))

    result = reste*(diviseur+1)
    for i in range(diviseur):
        result += 8*(i+1)
         
    return result

word = "abhrlngxyjkezwcm"
print(minimumPushes(word))