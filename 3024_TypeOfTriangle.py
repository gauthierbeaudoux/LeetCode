nums = [3,3,3]

def triangleType(nums: list[int]) -> str:
    if nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[2] + nums[1] > nums[0]:
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return "equilateral"
        if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        return "scalene"
    return "none"



print(triangleType(nums))