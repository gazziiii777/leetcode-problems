def missing_number(nums):
    n = len(nums)
    # Решено с помощью теоремы Гаусса. ((n * (n + 1)) // 2) - это сумма полного ряда, sum(nums) - это сумма ряда,где не хватает одного числа
    return ((n * (n + 1)) // 2) - sum(nums)


print(missing_number([9, 6, 4, 2, 3, 5, 8, 0, 1]))
