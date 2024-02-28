def check_Sorted(nums):
    small = nums[0]
    for index, number in enumerate(nums):
        if small <= number:
            small = number
        else:
            # break
            return False
    return True
    
a1 = [1,2,2,3,3,4]
a2 = [1,2,3,1,4]
print(check_Sorted(a2))