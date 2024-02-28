def largest(nums):
    large_num = nums[0]
    for index, number in enumerate(nums):
        if large_num < number:
            large_num = number
    return large_num

array = [2,4,6,16,7,9,8]
largest_number = largest(array)
print(largest_number)