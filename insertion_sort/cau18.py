def insert_right_to_left(a):
    arr=a.copy()
    n=len(arr)
    compare=0
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0:
            compare+=1
            if key<arr[j]:
                arr[j+1]=arr[j]
                j-=1
            else:
                break
        arr[j+1]=key
    return arr, compare


def insert_left_to_right(a):
    arr=a.copy()
    n=len(arr)
    compare=0
    for i in range(1, n):
        key=arr[i]
        insert_pos=i
        for j in range(i):
            compare+=1
            if key<arr[j]:
                insert_pos=j
                break
        for k in range(i,insert_pos,-1):
            arr[k]=arr[k-1]
        arr[insert_pos]=key
    return arr, compare


a1 = [1, 2, 4, 3, 5, 6, 7, 8]
a1_rl = insert_right_to_left(a1)
a1_lr = insert_left_to_right(a1)

a2 = [1, 2, 3, 4, 5, 6, 7, 8]
a2_rl = insert_right_to_left(a2)
a2_lr = insert_left_to_right(a2)

print(a1_rl)
print(a1_lr)
print("-"*20)
print(a2_rl)
print(a2_lr)