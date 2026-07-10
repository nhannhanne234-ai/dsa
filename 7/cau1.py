def question_one(a, k):
    left = max(a)
    right = sum(a)
    while left < right:
        mid = (left + right) // 2
        car = 1
        nums = 0
        for i in a:
            if nums + i <= mid:
                nums += i
            else:
                car += 1
                nums = i
        if car <= k:
            right = mid
        else:
            left = mid + 1
    print(left)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 5
print(question_one(a, k))