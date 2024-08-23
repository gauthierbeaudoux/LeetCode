expression = "-5/2+10/3+7/9"

def fractionAddition(expression: str) -> str:
    
    def calcul(a,b,c,d):
        num = a*d+b*c
        den = b*d
        
        i = 0
        nombre = [2,3,4,5,6,7,8,9]
        while i < len(nombre):
            if num % nombre[i] == 0 and den % nombre[i] == 0:
                num = num//nombre[i]
                den = den//nombre[i]
                i = 0
            else:
                i += 1
        
        return num, den
    
    def recup_nbr(expression, i):
        debut = i
        while i < len(expression) and expression[i] not in ['+','-','/']:
            i += 1
        return int(expression[debut:i]), i
        
    if len(expression) < 5:
        return expression
    
    i = 0
    liste = []
    while i < len(expression):
        # print(i)
        
        if expression[i] == '-':
            nbr, i = recup_nbr(expression, i+1)
            liste.append(-1*nbr)
            i += 1
        elif expression[i] == '/' or expression[i] == '+':
            i += 1
        else:
            nbr, i = recup_nbr(expression, i)
            liste.append(nbr)
            
        if len(liste) == 4:
            # print(liste)
            num, den = calcul(liste[0],liste[1],liste[2],liste[3])
            liste = [num, den]
    
    return f"{num}/{den}"


print(fractionAddition(expression))