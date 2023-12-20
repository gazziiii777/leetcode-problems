# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/submissions/?envType=daily-question&envId=2023-12-18

def max_product_difference(nums):
    nums_sorted = sorted(nums)
    return nums_sorted[-1] * nums_sorted[-2] - nums_sorted[0] * nums_sorted[1]


print(max_product_difference([4, 2, 5, 9, 7, 4, 8]))
