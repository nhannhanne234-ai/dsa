def count(a):
    count = 0
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j=i-1
        while (j>=0 and key<a[j]):
            a[j+1] = a[j]
            count+=1
            j-=1
        a[j+1] = key
    return count

a = [3, 2, 1]
result = count(a)
print(f"{result} lần dịch")