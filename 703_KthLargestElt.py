class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.a_renvoyer = k
        self.liste_nums = nums

    def add(self, val: int) -> int:
        self.liste_nums.append(val)
        self.liste_nums.sort()
        return self.liste_nums[-self.a_renvoyer]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)