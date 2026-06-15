def online_insertion_sort(a):
    arr = []
    for i in a:
        arr.append(i)
        key=i
        j=len(arr)-2
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
        print(arr, end=', ')
    return ''

a = [5, 2, 8, 1]
result = online_insertion_sort(a)
print(result)