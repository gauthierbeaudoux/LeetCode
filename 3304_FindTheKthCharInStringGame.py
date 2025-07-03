k = 5

def kthCharacter(k: int) -> str:
    initial = 1
    str_ini = str(initial)
    while len(str_ini) < k:
        to_be_added = "1"*len(str_ini)
        str_app = str(int(str_ini) + int(to_be_added))
        str_ini += str_app

    # print(str_ini)
    return chr(int(str_ini[k-1])+96)

print(kthCharacter(k))