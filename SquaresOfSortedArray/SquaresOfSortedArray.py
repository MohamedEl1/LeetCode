# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

nums = [-4, -1, 0, 3, 10]

for i in range(len(nums)):
    nums[i] = nums[i] ** 2


nums.sort()
print(nums)