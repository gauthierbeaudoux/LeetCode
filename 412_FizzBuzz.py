n = 3

def fizzBuzz(n: int) -> list[str]:
    L = []
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            L.append("FizzBuzz")
        elif i%3 == 0:
            L.append("Fizz")
        elif i%5 == 0:
            L.append("Buzz")
        else:
            L.append(f"{i}")
    return L


print(fizzBuzz(n))