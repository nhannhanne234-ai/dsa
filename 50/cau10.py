def binary_insertion_sort(a):
    n = len(a)
    compare = 0
    for i in range(1, n):
        left = 0
        right = i - 1
        key = a[i]
        while left <= right:
            mid = (left+right)//2
            compare += 1

            if a[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        j = i - 1
        while j >= left:
            a[j+1] = a[j]
            j-=1
        a[left] = key
    return a

a = [5, 2, 4, 6, 1, 3, 9, 8, 7]
result = binary_insertion_sort(a)
print(result)