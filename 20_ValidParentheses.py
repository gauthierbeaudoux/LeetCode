def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # depart = ["(","{","["]
    # arrivee = [")","}","]"]
    # couple = ["()","{}","[]"]

    depart = "({["
    arrivee = ")}]"
    couple = "(){}[]"
    indice_depart = []
    i = 0
    while i < len(s):
        if s[i] in depart:
            indice_depart.append(i)
            i += 1


        elif s[i] in arrivee:
            if len(indice_depart) == 0:
                return False
            elif s[indice_depart[-1]] + s[i] in couple:
                indice_depart.pop()

            # elif arrivee.index(s[i]) == depart.index(s[indice_depart[-1]]):
            #     indice_depart.pop()

            else:
                return False
            i += 1

        else:
            return False
        
    if len(indice_depart) == 0:
        return True
    
    return False
        

        
print(isValid("()"))