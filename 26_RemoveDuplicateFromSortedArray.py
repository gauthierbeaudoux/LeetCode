

# nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [-1,0,0,0,0,3,3]

# present = set()
# i = 0
# while i < len(nums):
#     if nums[i] not in present:
#         present.add(nums[i])
#         i += 1
#     else:
#         nums.remove(nums[i])

# print(nums)



present = sorted(set(nums))
nums = list(present)
print(nums)