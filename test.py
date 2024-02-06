L = [["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
 ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
 [9, 12, 8, 15, 14, 7]]


food = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]


from collections import Counter, defaultdict

mot1 = 'eat'
mot2 = 'tea'
a = defaultdict(list)
print(a)

a[2] = 3
print(a)

a[3].append(12)

print(a)