## 1. Phát biểu Bất biến vòng lặp (Loop Invariant)

Giả sử mảng ban đầu là a[0..n-1]. Thuật toán thực hiện một vòng lặp `for` với biến đếm i chạy từ 0 đến k-1. 

> **Phát biểu bất biến:** > Tại thời điểm ngay sau khi kết thúc vòng lặp thứ i (với 0 \le i \le k-1), đoạn mảng a[0..i] chứa đúng i+1 phần tử nhỏ nhất của toàn bộ mảng ban đầu, và các phần tử này đã được sắp xếp theo thứ tự tăng dần (a[0] \le a[1] \le \dots \le a[i]).

---

## 2. Chứng minh tính đúng đắn bằng Quy nạp toán học

Chúng ta sẽ chứng minh bất biến trên luôn đúng qua 3 bước: **Khởi tạo (Initialization)**, **Duy trì (Maintenance)**, và **Kết thúc (Termination)**.

### a. Bước khởi tạo (Initialization)
* **Thời điểm:** Ngay trước khi vòng lặp đầu tiên bắt đầu (i = 0 chưa chạy, có thể coi như vừa kết thúc vòng lặp tại bước i = -1).
* **Trạng thái:** Đoạn mảng a[0..-1] là một đoạn rỗng. Đoạn rỗng này hiển nhiên chứa 0 phần tử nhỏ nhất và đã được sắp xếp. 
* **Kết luận:** Bất biến đúng một cách hiển nhiên trước khi vào vòng lặp.

### b. Bước duy trì (Maintenance)
* **Giả thiết quy nạp:** Giả sử bất biến đúng sau vòng lặp thứ i - 1. Nghĩa là đoạn mảng a[0..i-1] đã chứa i phần tử nhỏ nhất của mảng ban đầu và được sắp xếp tăng dần. Đoạn còn lại a[i..n-1] chứa các phần tử lớn hơn hoặc bằng tất cả các phần tử trong a[0..i-1].
* **Hành động trong vòng lặp thứ i:** Thuật toán sẽ tìm phần tử nhỏ nhất trong đoạn còn lại a[i..n-1] (gọi là a[min\_idx]) rồi hoán đổi nó với a[i].
* **Phân tích:** * Vì a[min\_idx] là phần tử nhỏ nhất trong đoạn a[i..n-1], và theo giả thiết quy nạp, mọi phần tử trong đoạn này đều lớn hơn hoặc bằng các phần tử trong đoạn a[0..i-1], nên a[min\_idx] chắc chắn là phần tử nhỏ thứ i+1 của toàn bộ mảng.
    * Sau khi hoán đổi a[i] và a[min\_idx], phần tử nhỏ thứ i+1 này được đưa vào vị trí a[i]. 
    * Lúc này, đoạn mảng mới a[0..i] chính là đoạn a[0..i-1] cộng thêm phần tử a[i]. Do a[i] lớn hơn hoặc bằng mọi phần tử trong a[0..i-1], đoạn a[0..i] tiếp tục giữ nguyên tính chất được sắp xếp tăng dần và chứa đúng i+1 phần tử nhỏ nhất của mảng.
* **Kết luận:** Bất biến được duy trì sau khi kết thúc vòng lặp thứ i.

### c. Bước kết thúc (Termination)
* **Thời điểm:** Vòng lặp kết thúc khi biến đếm i đạt đến giá trị k (nghĩa là vòng lặp cuối cùng kết thúc tại i = k - 1).
* **Trạng thái:** Thay thế i = k - 1 vào phát biểu bất biến, ta được: Đoạn mảng a[0..k-1] chứa đúng (k-1) + 1 = k phần tử nhỏ nhất của toàn bộ mảng ban đầu, và đoạn này đã được sắp xếp theo thứ tự tăng dần.

---

## 3. Suy ra thuật toán đúng và dừng

* **Tính dừng (Termination):** Vòng lặp `for` có số bước lặp cố định là k bước (với k \le n), biến đếm i tăng tuyến tính sau mỗi vòng lặp nên thuật toán chắc chắn sẽ dừng sau đúng k lần lặp.
* **Tính đúng đắn (Correctness):** Từ kết quả ở bước **Kết thúc**, đoạn mảng a[0..k-1] chính là k phần tử nhỏ nhất cần tìm. Như vậy, thuật toán đã giải quyết chính xác yêu cầu đặt ra.