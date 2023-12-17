L = [["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
 ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
 [9, 12, 8, 15, 14, 7]]


food = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]


set_cuis = set(cuisines)

dic_test = {}
for i in set_cuis:
    dic_test[i] = []
print(dic_test)


for i in range(len(food)):
    dic_test[cuisines[i]].append(food[i])


print(dic_test)

print(dic_test["japanese"])