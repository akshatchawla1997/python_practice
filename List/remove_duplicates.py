"""remove duplicates from sorted array"""
def remove_dupli(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

arr = [1,1,2,2,2,3,3,4]
print(remove_dupli(arr))