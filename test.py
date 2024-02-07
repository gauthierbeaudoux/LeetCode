L = [["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
 ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
 [9, 12, 8, 15, 14, 7]]


food = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]


from collections import Counter, defaultdict

s = 'tree'

occ_s = Counter(s)


sorted_dic = dict(sorted(occ_s.items(), key=lambda x: -x[1]))
print(sorted_dic)
print(''.join([i*j for i,j in sorted_dic.items()]))