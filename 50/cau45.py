def count_subarrays(nums, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count

a = [1, 1, 1]
k = 2
print(count_subarrays(a, k))