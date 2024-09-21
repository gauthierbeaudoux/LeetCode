n = 13

def lexicalOrder(n: int) -> list[int]:
    liste = [i for i in range(1, n+1)]
    # print(liste)
    liste.sort(key= lambda x: str(x))
    # print(liste)
    return liste


print(lexicalOrder(n))