k = 10
operations = [0,1,0,1]

def kthCharacter(k: int, operations: list[int]) -> str:
    initial = 1
    str_ini = str(initial)
    i = 0
    while len(str_ini) < k:
        if operations[i] == 1:
            to_be_added = "1"*len(str_ini)
            str_app = str(int(str_ini) + int(to_be_added))
            str_ini += str_app
        else:
            str_ini += str_ini
        i += 1

    # print(str_ini)
    return chr(int(str_ini[k-1])+96)


print(kthCharacter(k, operations))