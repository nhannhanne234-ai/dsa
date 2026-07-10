def find_closest(a, x):
    if not a:
        return None
    
    closest_val = a[0]
    closest_idx = 0
    min_diff = abs(a[0] - x)
    
    for i in range(1, len(a)):
        current_diff = abs(a[i] - x)
        if current_diff < min_diff:
            min_diff = current_diff
            closest_val = a[i]
            closest_idx = i
            
    return closest_val, closest_idx

a16 = [10, 22, 28, 29, 40]
x16 = 26
print(find_closest(a16, x16))