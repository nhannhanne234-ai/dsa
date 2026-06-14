def find_you(a, x):
    if not a or not a[0]:
        return False
        
    m = len(a)
    n = len(a[0])
    
    left, right = 0, (m * n) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        row = mid // n
        col = mid % n
        
        element = a[row][col]
        
        if element == x:
            return True
        elif element < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

a = [[1, 3, 5], [7, 9, 11]]
x = int(input("Nhập: "))
result = find_you(a, x)

print(f"Thấy thằng số {x} (x = {x}) trong ma trận không m? -> {result}")