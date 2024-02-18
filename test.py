L = [["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
 ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
 [9, 12, 8, 15, 14, 7]]


food = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]


from collections import Counter, defaultdict

income = {'Anne' : 1111,
          'Bert' : 2222,
          'Cara' : 9999999}

print(min(income, key=income.get))
# Anne