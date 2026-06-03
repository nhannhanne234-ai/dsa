def sqrt(n):
    if n < 2:
        return n
    
    left = 0
    right = n //2
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        mid_squard = mid * mid

        if mid_squard == n:
            return mid
        elif mid_squard < n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans
    
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for n in lst:
n = int(input("Nhập: "))
print({sqrt(n)})