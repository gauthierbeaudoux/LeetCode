a = "11"
b = "1"

def addBinary(a,b):
    a2 = int(a, base=2)
    b2 = int(b, base=2)
    return str(bin(a2+b2)[2:])


print(addBinary(a,b))

