def find_k_closest_elements(a, k, x):
    left, right = 0, len(a) - k
    
    while left < right:
        mid = (left + right) // 2
        
        if x - a[mid] > a[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return a[left : left + k]

a = [1, 2, 3, 4, 5]
k = 4
x = 3
result = find_k_closest_elements(a, k, x)

print(f"{k} phần tử gần {x} nhất là: {result}")