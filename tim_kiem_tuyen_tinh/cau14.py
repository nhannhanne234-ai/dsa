def find_first_even(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1

a14 = [3, 7, 11, 8, 5, 4]
print(find_first_even(a14))