def ten_sv(ds, x):
    for i in range(len(ds)):
        if ds[i] == x: 
            return i
        
    else: 
        return -1


ds = ["Nhan", "Anh", "Hau"]
x = input('Nhap ten: ').title()

kqua = ten_sv(ds, x)
print(f'vi tri: {kqua}')