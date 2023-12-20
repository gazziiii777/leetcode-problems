# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return i, i + 1


print(two_sum([2, 7, 11, 15], 9))
