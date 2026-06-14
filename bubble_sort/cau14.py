def cocktail_shaker_sort(a):

    left = 0
    right = len(a) - 1

    while left < right:
        swapped = False

# loop này đẩy lớn về cuối
        for i in range(left, right):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        right -= 1                                  # sau lượt này số lớn nhất đã ở cuối nên không chạy về cuối nữa

        if swapped == False:                         # chạy suôi không có swapped thì dừng
            break

        swapped = False                             # reset cờ lại

# loop này đẩy nhỏ về đầu
        for i in range(right, left, -1):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
                swapped = True

        left += 1                                   # sau lượt này nhỏ lớn nhất đã ở nên nên không chạy về đầu nữa nữa

        if swapped == True:
            break

    return a

a = [5, 1, 4, 2, 8]
print(cocktail_shaker_sort(a))