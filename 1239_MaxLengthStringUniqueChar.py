from collections import Counter

arr = ["un","iq","ue"]
arr = ["cha","r","act","ers"]

def maxLength(arr: list[str]) -> int:
    i = 0
    while i < len(arr):
        mot_occ = Counter(arr[i])
        for j in mot_occ.values():
            if j > 1:
                arr.pop(i)
                break
        else:
            i += 1
    def cout_max(arr):
        if len(arr) == 0:
            return 0
        else:
            longueur_max = -1
            for mot in arr:
                result = mot
                copie_arr = arr[:]
                for lettre in mot:
                    i = 0
                    while i < len(copie_arr):
                        if lettre in copie_arr[i]:
                            copie_arr.pop(i)
                        else:
                            i += 1
                longueur = len(result) + cout_max(copie_arr)
                if longueur > longueur_max:
                    longueur_max = longueur
            return longueur_max
    return cout_max(arr)
                    


# print(maxLength(arr))


# A Comprendre


def maxLength(arr: list[str]) -> int:
    l=[set()]
    print(arr)
    for i in arr:
        if len(set(i)) < len(i):
            continue
        i = set(i)
        print(f"i : {i}")
        for j in l:
            print(f"j : {j}")
            if i & j:
                continue
            l.append(i | j)
            print(f"l : {l}")
    m = 0
    for i in l:
        if m < len(i):
            m = len(i)
    return m

print(maxLength(arr))