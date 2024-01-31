temperatures = [73,74,75,71,69,72,76,73]

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    temp_days = {}
    result = {}
    for i in range(len(temperatures)):
        temp_days[i] = temperatures[i]
        to_delete = []
        for indice, temp in temp_days.items():
            if temperatures[i] > temp:
                result[indice] = i-indice
                to_delete.append(indice)
        for i in to_delete:
            del temp_days[i]
    for indice, temp in temp_days.items():
        result[indice] = 0
    return [result[i] for i in range(len(temperatures))]


print(dailyTemperatures(temperatures))