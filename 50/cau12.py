# bubble
def stability(a):
    n = len(a)
    for j in range(n-1):
        swapped = False
        for i in range(n-1-j):
            condition1 = a[i][0] > a[i+1][0]                                    # so sánh ở index 0 cái nào lớn hơn (number)
            condition2 = (a[i][0] == a[i+1][0]) and (a[i][1] > a[i+1][1])       # hai số bằng nhau thì qua index 1 so sánh chữ (letter)
            if condition1 or condition2:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if swapped == False:
            break
    return a

a = [(2,'a'),(1,'b'),(2,'c')]
print(stability(a))



# insertion
def base_insert(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j=i-1
        while j>=0:
            condition1 = (key[0] < a[j][0]) 
            condition2 = (key[0] == a[j][0]) and (key[1] < a[j][1])
            if condition1 or condition2:
                a[j+1] = a[j]
                j-=1
            else:
                break
        a[j+1]=key
    return a

a = [(2,'c'),(1,'b'),(2,'a')]
result = base_insert(a)
print(result)



# selection
def stable_selection_sort(a: list) -> list:
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key
    return a

a = [(2, 'a'), (2, 'b'), (1, 'c')]
print(stable_selection_sort(a))

def demonstrate_instability():
    a = [(2, 'a'), (2, 'b'), (1, 'c')]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

print(demonstrate_instability())