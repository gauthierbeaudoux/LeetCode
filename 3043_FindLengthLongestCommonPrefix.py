arr1 = [1,10,100], arr2 = [1000]

def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
    arr1.sort()
    arr2.sort()

print(longestCommonPrefix(arr1, arr2))