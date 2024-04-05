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


nums = [1,2,2,3,1,4]
occ_nums = Counter(nums)
print(occ_nums)
print(occ_nums.get(5, 0))

L = [(4,5), (2,3)]
print(L)

print((4,3) in L)

print("a" == "A")



