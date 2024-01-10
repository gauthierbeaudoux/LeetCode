L = [["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
 ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
 [9, 12, 8, 15, 14, 7]]


food = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]



dic_node = {1: [5, 3], 5: [4], 4: [9, 2], 3: [10, 6]}
print(dic_node)
list_infected = [3]
# while len(dic_node) > 0:
x = list_infected[0]
list_infected.pop(0)
if x in dic_node:
    for value in dic_node[x]:
        list_infected.append(value)
    del dic_node[x]
list_to_delete = []
for key, value in dic_node.items():
    if x in value:
        list_to_delete.append(key)
        list_infected.append(key)
        for y in value:
            if y != x:
                list_infected.append(y)
for i in list_to_delete:
    del dic_node[i]

print(dic_node)

print(list_infected)