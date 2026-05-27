def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    else:
        return -1


a = [7, 3, 9, 12, 5, 8, 1]
x = int(input("Nhap gia tri can tim: "))

kqua = linear_search(a, x)

if kqua != -1:
    print(f"Tim thay {x} tai vi tri: {kqua}")
else:
    print(f"Khong tim thay {x} trong mang a")