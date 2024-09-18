nums = [10,2]

def largestNumber(nums: list[int]) -> str:
    list_str = [str(i) for i in nums]
    list_str.sort(key = lambda x: x*10, reverse=True)
    result = "".join(list_str)
    if result[0] == "0":
        return "0"
    return result
    
    
print(largestNumber(nums))