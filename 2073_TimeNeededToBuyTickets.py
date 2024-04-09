tickets = [2,3,2]
k = 2


def timeRequiredToBuy(tickets: list[int], k: int) -> int:
    compteur = 0
    n = len(tickets)
    while True:
        for i in range(n):
            if tickets[i] > 0:
                tickets[i] -= 1
                compteur += 1
            
            if i == k and tickets[k] == 0:
                return compteur

print(timeRequiredToBuy(tickets, k))