from math import isqrt
import heapq

gifts = [25,64,9,4,100]
k = 4

def pickGifts(gifts: list[int], k: int) -> int:
    for _ in range(k):
        # Premiere version

        # maxi = max(gifts)
        # idx_max = gifts.index(maxi)
        # gifts[idx_max] = int(maxi**0.5)

        # Deuxieme version
        gifts = sorted(gifts)
        gifts[-1] = isqrt(gifts[-1])
        
    return sum(gifts)


def version_heap(gifts: list[int], k: int) -> int:
    heap = []
    for item in gifts:
        heapq.heappush(heap, -item)

    m = -heapq.heappop(heap)
    for _ in range(k):
        m = -heapq.heappushpop(heap, -isqrt(m))
    return m - sum(heap)

# print(pickGifts(gifts, k))

print(version_heap(gifts, k))
