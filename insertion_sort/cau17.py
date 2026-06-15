def shift_count(a):
    n = len(a)
    count = 0
    for i in range(1,n):
        key = a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
            count+=1
        a[j+1]=key
    return a,count

a = [1, 2, 4, 3, 5]
sort_a, shift_a = shift_count(a)
print(f"chỉ {shift_a} shift")