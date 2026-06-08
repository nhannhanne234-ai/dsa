1. Phát biểu Bất biến vòng lặp (Loop Invariant) 

    Trước khi bắt đầu vòng lặp ngoài (với biến chỉ số j), đoạn mảng cuối cùng gồm j phần tử đã được sắp xếp hoàn toàn và chứa đúng j phần tử lớn nhất của toàn bộ mảng.


2. Chứng minh bằng Quy nạp toán học

    Bước 1: Khởi tạo (Initialization)
        Khi j = 0 (vòng lặp chưa chạy): Số phần tử ở cuối mảng là $0$. Mệnh đề hiển nhiên đúng.

    Bước 2: Duy trì (Maintenance)
        Giả sử sau lượt j, mảng đã có j phần tử lớn nhất đứng đúng chỗ ở cuối. Ở lượt quét tiếp theo (j+1), vòng lặp trong (biến i) sẽ duyệt từ đầu mảng đến vị trí n - j - 1. Cơ chế hoán đổi liên kề if a[i] > a[i+1] sẽ liên tục đẩy phần tử lớn nhất còn lại trong đoạn lộn xộn về phía bên phải. Khi vòng lặp trong kết thúc, phần tử này sẽ đứng ngay trước đoạn đã sắp xếp. Số phần tử lớn nhất đứng đúng chỗ tăng lên thành j + 1. Bất biến được duy trì.
 
    Bước 3: Hoàn thành (Termination)
        Vòng lặp ngoài kết thúc khi j = n - 1. Theo tính chất bất biến, đoạn mảng cuối đã chứa đúng n - 1 phần tử lớn nhất và được sắp xếp. Phần tử duy nhất còn lại ở vị trí đầu tiên (a[0]) bắt buộc phải là phần tử nhỏ nhất.
    
    
---> Kết luận: Thuật toán dừng lại và mảng được sắp xếp đúng hoàn toàn. 