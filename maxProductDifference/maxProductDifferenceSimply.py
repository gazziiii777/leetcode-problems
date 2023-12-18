nums = [4,2,5,9,7,4,8]

def maxProductDifference(nums):
    numsSorted = sorted(nums)
    return numsSorted[-1] * numsSorted[-2] - numsSorted[0] * numsSorted[1]

print(maxProductDifference(nums))