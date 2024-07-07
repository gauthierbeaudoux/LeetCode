numBottles = 9
numExchange = 3


def numWaterBottles(numBottles: int, numExchange: int) -> int:
    result = numBottles
    nb_vides = numBottles
    while nb_vides >= numExchange:
        result += nb_vides // numExchange
        nb_vides = nb_vides%numExchange + nb_vides//numExchange
    return result
    


print(numWaterBottles(numBottles, numExchange))