def find_min_rotated_array(a):
    left, right = 0, len(a) - 1
    
    if a[left] <= a[right]:
        return a[left]
        
    while left < right:
        mid = (left + right) // 2
        
        if a[mid] > a[right]:
            left = mid + 1
        else:
            right = mid
            
    return a[left]

a = [3, 4, 5, 1, 2]
result = find_min_rotated_array(a)

print(f"Không lọt vào mắt luôn á số {result} à")