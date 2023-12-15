paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]


def destCity(paths: list[list[str]]) -> str:
    liste_depart = [ville[0] for ville in paths]
    liste_arrivee = [ville[1] for ville in paths]
    for i in liste_arrivee:
        if i not in liste_depart:
            return i


print(destCity(paths))