def target_2_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return num_dict[complement], i
        num_dict[num] = i
    return None
    
    # first_element = nums[len(nums)-1]
    # for i in range(1,len(nums)):
    #     sum = 0
    #     for index, number in enumerate(nums):
    #         sum = number + first_element
    #         if sum == target:
    #             return index, nums.index(first_element)
    #     else:
    #         first_element = nums[i]

        

array = [3,3]
achievement = target_2_sum(array, 6)
print(achievement)