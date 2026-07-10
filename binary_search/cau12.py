def find_peak(a):
    left, right = 0, len(a) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if a[mid] < a[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return left

a = [1, 2, 3, 1]
peak_index = find_peak(a)

print(f"Ôi sao cao thế số {peak_index}")