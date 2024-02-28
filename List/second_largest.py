def second_largest(nums):
    f_largest, s_largest = nums[0], nums[0]
    for i in nums:
        if i > f_largest:
            s_largest = f_largest
            f_largest = i
        elif i > s_largest and i != f_largest:
            s_largest = i
    return s_largest

array = [1,2,9,7,7,5]

print(second_largest(array))