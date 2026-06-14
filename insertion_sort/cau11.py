def absolute_cure(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i - 1

        while j >= 0:
            key_square = key**2
            a_j_square = a[j]**2
            move = False

            if key_square < a_j_square:
                move = True
            elif key_square == a_j_square:
                if key < 0 and a[j] > 0:
                    move = True

            if move:
                a[j+1] = a[j]
                j-=1
            else:
                break
            
        a[j+1] = key
    return a

a = [4, 8, -8, -3, 1, -2, 2]
result = absolute_cure(a)
print(result)