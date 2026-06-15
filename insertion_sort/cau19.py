def gnome_sort(a):
    n=len(a)
    index=0
    while index<n:
        if index==0:
            index+=1
        elif a[index]>=a[index-1]:
            index+=1
        else:
            a[index],a[index-1]=a[index-1],a[index]
            index-=1
    return a

a = [3, 2, 1]
result = gnome_sort(a)
print(result)