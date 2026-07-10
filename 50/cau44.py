def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return (seen[complement], i)
        seen[nums[i]] = i
    return None

a = [2, 7, 11]
target = 9
print(two_sum(a, target))