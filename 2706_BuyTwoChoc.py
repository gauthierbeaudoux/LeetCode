prices = [3,2,3]
money = 3


def buyChoco(prices: list[int], money: int) -> int:
    prices.sort()
    if prices[0] + prices[1] <= money:
        return money - (prices[0] + prices[1])
    return money


print(buyChoco(prices,money))