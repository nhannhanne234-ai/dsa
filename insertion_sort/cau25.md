1. Phát biểu Bất biến vòng lặp (Loop Invariant)
    - Đối với vòng lặp for ngoài cùng với biến chạy i (chạy từ 1 đến n-1), bất biến vòng lặp được phát biểu như sau:
    - Phát biểu: > Tại thời điểm trước mỗi vòng lặp ngoài thứ i, đoạn mảng con A[0..i-1] luôn chứa đúng các phần tử ban đầu thuộc các vị trí từ 0 đến i-1, nhưng các phần tử này đã được sắp xếp theo thứ tự tăng dần.

2. Chứng minh tính đúng đắn bằng Quy nạp Toán học
    - Để chứng minh bất biến vòng lặp luôn đúng, ta cần chỉ ra 3 thuộc tính: Khởi tạo (Initialization), Duy trì (Maintenance), và Kết thúc (Termination).

    a. Khởi tạo (Initialization) - Bước cơ sở
        - Thời điểm: Trước khi vòng lặp bắt đầu chạy lần đầu tiên (tức là khi i = 1).
        - Kiểm tra: Đoạn mảng con lúc này chỉ gồm một phần tử duy nhất là A[0..0] (hay chính là phần tử A[0]).
        - Kết luận: Một mảng chỉ chứa duy nhất một phần tử thì hiển nhiên luôn chứa các phần tử ban đầu và luôn luôn được coi là đã sắp xếp. Do đó, bất biến vòng lặp ĐÚNG tại bước khởi tạo.

    b. Duy trì (Maintenance) - Bước quy nạp
        - Giả thiết: Giả sử bất biến vòng lặp đúng trước vòng lặp thứ i. Nghĩa là đoạn mảng A[0..i-1] đã được sắp xếp tăng dần.
        - Hành vi trong vòng lặp: Vòng lặp trong (vòng lặp chèn) sẽ lấy phần tử khóa key = A[i] và so sánh ngược về phía trước với các phần tử trong đoạn A[0..i-1].
            + Các phần tử lớn hơn key sẽ được dịch chuyển (shift) sang phải 1 vị trí để chừa khoảng trống.
            + Khi tìm được vị trí thích hợp (nơi không còn phần tử nào lớn hơn key), phần tử key sẽ được chèn vào vị trí đó.
        - Kết quả sau vòng lặp: Hành động này giúp mở rộng đoạn mảng đã sắp xếp từ A[0..i-1] thành đoạn mảng A[0..i]. Đoạn mảng mới này chứa chính xác các phần tử ban đầu của đoạn A[0..i] nhưng đã nằm đúng thứ tự tăng dần.
        - Kết luận: Khi biến chạy tăng lên i + 1 để chuẩn bị cho vòng lặp kế tiếp, đoạn mảng A[0..(i+1)-1] (tức là A[0..i]) đã được sắp xếp. Do đó, bất biến vòng lặp được DUY TRÌ.

    c. Kết thúc (Termination)
        - Thời điểm: Vòng lặp dừng lại khi điều kiện vòng lặp ngoài không còn thỏa mãn, tức là khi biến chạy i = n (với n là tổng số phần tử của mảng A).
        - Thay i = n vào phát biểu bất biến: Trước vòng lặp thứ n (vòng lặp không xảy ra do đã hết phần tử), đoạn mảng con A[0..n-1] chứa đúng các phần tử ban đầu của mảng, nhưng đã được sắp xếp theo thứ tự tăng dần.
        - Kết luận: Vì đoạn mảng A[0..n-1] chính là toàn bộ mảng ban đầu A, điều này đồng nghĩa với việc toàn bộ mảng A đã được sắp xếp thành công.

3. Kết luận chung
    - Vì bất biến vòng lặp đã thỏa mãn cả 3 tính chất: Khởi tạo, Duy trì và Kết thúc, ta đi đến kết luận: Thuật toán Insertion Sort hoàn toàn đúng đắn.