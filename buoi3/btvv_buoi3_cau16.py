def adversity(a):
    n = len(a)
    swap = 0
    for j in range(n-1):
        for i in range(n-1-j):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swap +=1
    return swap

a = [2, 3, 1]
result = adversity(a)
print(f"{result} nghịch thế = {result} swap")