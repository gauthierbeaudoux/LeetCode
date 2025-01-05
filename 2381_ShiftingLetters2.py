s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]

def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
    # a = 97 et z = 122
    liste_s = [ord(i) for i in s]
    # print(liste_s)
    for i in shifts:
        if i[2] == 0:
            liste_s[i[0]:i[1]+1] = [j-1 for j in liste_s[i[0]:i[1]+1]]
        elif i[2] == 1:
            liste_s[i[0]:i[1]+1] = [j+1 for j in liste_s[i[0]:i[1]+1]]
        else:
            raise Exception("Erreur")
        # print(liste_s)
    
        
    return "".join([chr((i-97)%26 + 97) for i in liste_s])
            
                


print(shiftingLetters(s, shifts))
